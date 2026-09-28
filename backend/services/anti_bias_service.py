import re
import json
from typing import List, Tuple, Dict, Any, Optional
from backend.config import BRANDS_GAZETTEER_PATH, SUPERSEDED_MAPPING_PATH
from backend.models.schemas import BiasViolation, ComplianceAuditResult

class AntiBiasService:
    def __init__(self):
        self.brands_data = self._load_json(BRANDS_GAZETTEER_PATH, "brands", [])
        self.superseded_data = self._load_json(SUPERSEDED_MAPPING_PATH, None, {})

    def _load_json(self, path, key=None, default=None):
        if path.exists():
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = json.load(f)
                    return content.get(key, default) if key else content
            except Exception:
                return default
        return default

    def audit_specification(self, raw_text: str) -> ComplianceAuditResult:
        violations: List[BiasViolation] = []
        health_score = 100
        
        # 1. Check for Brand Name Violations & 'Or Equivalent' Compliance
        brand_violations = self._check_brand_bias(raw_text)
        violations.extend(brand_violations)
        
        # 2. Check for Superseded / Obsolete Indian Standards
        superseded_violations = self._check_superseded_standards(raw_text)
        violations.extend(superseded_violations)

        # 3. Check for Foreign Standards when Indian Standards are expected
        foreign_violations = self._check_foreign_standards(raw_text)
        violations.extend(foreign_violations)

        # 4. Calculate Health Score
        for v in violations:
            if v.severity == "CRITICAL":
                health_score -= 25
            elif v.severity == "WARNING":
                health_score -= 15
            elif v.severity == "INFO":
                health_score -= 5

        health_score = max(0, min(100, health_score))
        is_gfr_compliant = (health_score >= 85 and not any(v.severity == "CRITICAL" for v in violations))

        # Generate mandatory tender compliance clauses
        mandatory_clauses = [
            "Specifications must be interpreted as generic and functional in accordance with GFR 2017 Rule 144(i).",
            "Any reference to specific trade names, brands, or proprietary catalogs shall implicitly mean 'or equivalent conforming to the relevant Indian Standard'."
        ]

        return ComplianceAuditResult(
            health_score=health_score,
            is_gfr_compliant=is_gfr_compliant,
            is_qco_mandatory=False,  # Evaluated after standards recommendation
            qco_order_title=None,
            qco_ministry=None,
            violations_count=len(violations),
            violations=violations,
            mandatory_clauses_to_insert=mandatory_clauses
        )

    def _check_brand_bias(self, text: str) -> List[BiasViolation]:
        violations = []
        lower_text = text.lower()

        for idx, brand_info in enumerate(self.brands_data):
            b_name = brand_info["name"]
            pattern = r'\b' + re.escape(b_name.lower()) + r'\b'
            match = re.search(pattern, lower_text)
            
            if match:
                # Check proximity for 'or equivalent' within next 100 characters
                end_pos = match.end()
                window = text[end_pos:end_pos + 120]
                equiv_pattern = re.compile(r'\b(?:or\s+equivalent|or\s+better|or\s+higher)\b', re.IGNORECASE)
                
                if equiv_pattern.search(window):
                    violations.append(BiasViolation(
                        violation_id=f"BIAS-BRAND-{idx+1}",
                        type="BRAND_NAME_CITATION",
                        severity="WARNING",
                        offending_text=f"'{b_name}' cited with 'or equivalent'",
                        gfr_rule="Rule 144(i)(b)",
                        explanation=(
                            f"Brand '{b_name}' is referenced. Although 'or equivalent' is included, "
                            f"GFR 144(i)(b) advises defining functional characteristics directly rather than naming specific manufacturers."
                        ),
                        suggested_replacement=brand_info["recommended_generic_replacement"]
                    ))
                else:
                    violations.append(BiasViolation(
                        violation_id=f"BIAS-BRAND-{idx+1}",
                        type="BRAND_NAME_BIAS",
                        severity="CRITICAL",
                        offending_text=b_name,
                        gfr_rule="Rule 144(i)(b)",
                        explanation=(
                            f"Direct specification of brand '{b_name}' without the mandatory 'or equivalent' suffix. "
                            f"This restricts open competition and creates an unfair vendor lock-in under GFR 2017 Rule 144(i)."
                        ),
                        suggested_replacement=f"{brand_info['recommended_generic_replacement']} (or equivalent)"
                    ))

        return violations

    def _check_superseded_standards(self, text: str) -> List[BiasViolation]:
        violations = []
        idx = 1
        for old_code, meta in self.superseded_data.items():
            pattern = r'\b' + re.escape(old_code) + r'\b'
            if re.search(pattern, text, re.IGNORECASE):
                violations.append(BiasViolation(
                    violation_id=f"BIAS-SUPERSEDED-{idx}",
                    type="SUPERSEDED_STANDARD",
                    severity="WARNING",
                    offending_text=old_code,
                    gfr_rule="Rule 144(i)(c)",
                    explanation=(
                        f"Tender references '{old_code}' which has been SUPERSEDED by BIS with '{meta['superseded_by']}'. "
                        f"Reason: {meta['reason']}. Citing obsolete standards leads to supply disputes or rejection of deliveries."
                    ),
                    suggested_replacement=f"{meta['superseded_by']} ({meta['title']})"
                ))
                idx += 1
        return violations

    def _check_foreign_standards(self, text: str) -> List[BiasViolation]:
        violations = []
        foreign_standards = [
            ("ASTM A53", "IS 1239 (Part 1):2004 (Steel Tubes/Pipes)"),
            ("ASTM A615", "IS 1786:2008 (High Strength Deformed Steel Bars)"),
            ("DIN 4102", "IS 3809 (Fire Resistance Test for Structures)"),
            ("BS 5308", "IS 1554 / IS 694 (Control & Power Cables)")
        ]
        for idx, (foreign_code, is_replacement) in enumerate(foreign_standards):
            if re.search(r'\b' + re.escape(foreign_code) + r'\b', text, re.IGNORECASE):
                violations.append(BiasViolation(
                    violation_id=f"BIAS-FOREIGN-{idx+1}",
                    type="FOREIGN_STANDARD_BIAS",
                    severity="WARNING",
                    offending_text=foreign_code,
                    gfr_rule="Rule 144(i)(d)",
                    explanation=(
                        f"Tender cites foreign standard '{foreign_code}'. Under GFR 144(i)(d), national standards (BIS) "
                        f"must be prioritized whenever an applicable Indian Standard exists."
                    ),
                    suggested_replacement=f"{is_replacement} (or equivalent international standard)"
                ))
        return violations

    def sanitize_text(self, raw_text: str, audit_result: ComplianceAuditResult) -> str:
        """Automatically rewrite specification text by neutralizing brands and updating obsolete standards."""
        sanitized = raw_text
        
        # Replace brands
        for b_info in self.brands_data:
            b_name = b_info["name"]
            replacement = b_info["recommended_generic_replacement"]
            pattern = re.compile(r'\b(?:strictly\s+sourced\s+from\s+)?' + re.escape(b_name) + r'(?:\s+or\s+[A-Za-z0-9]+)?(?:\s+manufacturer\s+catalogue)?\b', re.IGNORECASE)
            if pattern.search(sanitized):
                sanitized = pattern.sub(f"{replacement} (or equivalent conforming to relevant Indian Standard)", sanitized)

        # Replace superseded standards
        for old_code, meta in self.superseded_data.items():
            pattern = re.compile(r'\b' + re.escape(old_code) + r'\b', re.IGNORECASE)
            if pattern.search(sanitized):
                sanitized = pattern.sub(f"{meta['superseded_by']} (Latest Revision - superseding {old_code})", sanitized)

        return sanitized
