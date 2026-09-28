import json
from typing import List, Dict, Any, Optional
from backend.config import QCO_REGISTRY_PATH
from backend.models.schemas import ComplianceAuditResult, StandardRecommendation

class ComplianceService:
    def __init__(self):
        self.qco_records = self._load_qco_records()

    def _load_qco_records(self) -> List[Dict[str, Any]]:
        if QCO_REGISTRY_PATH.exists():
            try:
                with open(QCO_REGISTRY_PATH, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def verify_statutory_qco(
        self,
        audit_result: ComplianceAuditResult,
        top_recommendations: List[StandardRecommendation]
    ) -> ComplianceAuditResult:
        """Cross-references recommended standards with statutory Quality Control Orders."""
        if not top_recommendations:
            return audit_result

        primary_recommendation = top_recommendations[0]
        base_code = primary_recommendation.base_code.strip()

        for qco in self.qco_records:
            mandatory_list = [c.strip() for c in qco.get("mandatory_standards", [])]
            if base_code in mandatory_list:
                audit_result.is_qco_mandatory = True
                audit_result.qco_order_title = qco["order_title"]
                audit_result.qco_ministry = qco["issuing_ministry"]
                
                # Add statutory compliance clause for tender specification
                statutory_clause = (
                    f"STATUTORY QUALITY MANDATE: As per the '{qco['order_title']}' notified by the "
                    f"{qco['issuing_ministry']} under Section 16 of the BIS Act 2016 ({qco['gazette_notification_no']}), "
                    f"bidders must hold a valid BIS License to use the Standard Mark (ISI Mark) conforming to {base_code}. "
                    f"Bids without valid BIS certification shall be summarily rejected at technical evaluation."
                )
                if statutory_clause not in audit_result.mandatory_clauses_to_insert:
                    audit_result.mandatory_clauses_to_insert.insert(0, statutory_clause)
                break

        return audit_result
