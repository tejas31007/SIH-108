import json
from datetime import datetime
from backend.models.schemas import ExportRequest, ExportResponse

class ExportService:
    @staticmethod
    def generate_export(request: ExportRequest) -> ExportResponse:
        date_str = datetime.now().strftime("%d-%B-%Y")
        clean_filename_base = request.tender_title.lower().replace(" ", "_")[:30]

        if request.export_format == "json":
            content_dict = {
                "document_type": "GeM_Compliant_Procurement_Specification",
                "generated_at": datetime.now().isoformat(),
                "tender_title": request.tender_title,
                "applicable_indian_standard": {
                    "is_code": request.selected_standard.is_code,
                    "title": request.selected_standard.title,
                    "status": request.selected_standard.status,
                    "is_qco_mandatory": request.selected_standard.mandatory_qco,
                    "qco_ministry": request.selected_standard.qco_ministry
                },
                "gfr_compliance_score": request.compliance_audit.health_score,
                "sanitized_specification": request.sanitized_text,
                "statutory_clauses": request.compliance_audit.mandatory_clauses_to_insert,
                "clause_citations": [c.model_dump() for c in request.selected_standard.clause_citations]
            }
            return ExportResponse(
                format="json",
                content=json.dumps(content_dict, indent=2),
                download_filename=f"procurement_spec_{clean_filename_base}.json"
            )

        elif request.export_format == "html":
            html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Procurement Specification - {request.tender_title}</title>
    <style>
        body {{ font-family: 'Segoe UI', Arial, sans-serif; margin: 40px; color: #1e293b; line-height: 1.6; }}
        .header {{ border-bottom: 2px solid #0f172a; padding-bottom: 16px; margin-bottom: 24px; }}
        .badge {{ display: inline-block; padding: 4px 10px; border-radius: 9999px; font-size: 12px; font-weight: bold; background: #e0f2fe; color: #0369a1; }}
        .badge-qco {{ background: #fee2e2; color: #b91c1c; }}
        .card {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin-bottom: 20px; }}
        h1, h2, h3 {{ color: #0f172a; }}
        .specs {{ white-space: pre-wrap; font-family: inherit; background: #ffffff; padding: 16px; border: 1px solid #cbd5e1; border-radius: 6px; }}
        .clause-item {{ border-left: 3px solid #3b82f6; padding-left: 12px; margin-bottom: 12px; }}
    </style>
</head>
<body>
    <div class="header">
        <h2>GOVERNMENT OF INDIA - PUBLIC PROCUREMENT TENDER ANNEXURE</h2>
        <h3>Schedule of Technical Specifications & Standards Compliance</h3>
        <p><strong>Tender Title:</strong> {request.tender_title} | <strong>Date:</strong> {date_str}</p>
        <p><strong>GFR 144(i) Compliance Rating:</strong> <span class="badge">{request.compliance_audit.health_score}/100 [Audited]</span></p>
    </div>

    <div class="card">
        <h3>Applicable National Standard</h3>
        <p><strong>Indian Standard:</strong> {request.selected_standard.is_code} ({request.selected_standard.title})</p>
        <p><strong>Division:</strong> {request.selected_standard.division_name} | <strong>Status:</strong> {request.selected_standard.status}</p>
        {'<p><span class="badge badge-qco">MANDATORY QUALITY CONTROL ORDER IN FORCE</span></p>' if request.selected_standard.mandatory_qco else ''}
    </div>

    <div class="card">
        <h3>Sanitized Generic Technical Specifications (GFR 144(i) Neutralized)</h3>
        <div class="specs">{request.sanitized_text}</div>
    </div>

    <div class="card">
        <h3>Statutory Tender Clauses & Instructions</h3>
        <ul>
            {''.join([f"<li>{c}</li>" for c in request.compliance_audit.mandatory_clauses_to_insert])}
        </ul>
    </div>

    <div class="card">
        <h3>Clause-Level Alignment & Audit Justification</h3>
        {''.join([f'<div class="clause-item"><strong>{c.clause_number} ({c.clause_title})</strong>: {c.alignment_reason}<br><small style="color:#64748b;">Excerpt: {c.standard_text_snippet}</small></div>' for c in request.selected_standard.clause_citations])}
    </div>
</body>
</html>"""
            return ExportResponse(
                format="html",
                content=html_content,
                download_filename=f"procurement_spec_{clean_filename_base}.html"
            )

        else: # Markdown
            md_content = f"""# Government of India - Public Procurement Tender Specification
## Technical Specification Schedule & Standards Compliance Annexure

**Tender Reference / Subject:** {request.tender_title}  
**Date of Audit:** {date_str}  
**GFR 2017 Rule 144(i) Compliance Health Score:** `{request.compliance_audit.health_score} / 100`  

---

### 1. Applicable National Standard (BIS)
* **Standard Code:** **`{request.selected_standard.is_code}`**
* **Title:** {request.selected_standard.title}
* **Division:** {request.selected_standard.division_name}
* **Operational Status:** `{request.selected_standard.status}`
* **Quality Control Order (QCO):** {"**YES - MANDATORY CERTIFICATION REQUIRED**" if request.selected_standard.mandatory_qco else "Voluntary / General Specification"}
* **Governing Ministry:** {request.selected_standard.qco_ministry or "Bureau of Indian Standards"}

---

### 2. Sanitized Generic Technical Specifications
*(Audited and neutralized in strict adherence to GFR 144(i) non-discrimination guidelines)*

{request.sanitized_text}

---

### 3. Mandatory Statutory Tender Clauses
The following clauses are statutory conditions of contract for bidders:
{chr(10).join([f"- **Clause {i+1}:** {c}" for i, c in enumerate(request.compliance_audit.mandatory_clauses_to_insert)])}

---

### 4. Clause-Level Compliance & Standards Alignment
{chr(10).join([f"* **{c.clause_number} ({c.clause_title}):** {c.alignment_reason}  {chr(10)}  > *Standard Requirement:* \"{c.standard_text_snippet}\"" for c in request.selected_standard.clause_citations])}

---
*Generated by BharatStandards AI Recommendation Engine (SIH26108)*
"""
            return ExportResponse(
                format="markdown",
                content=md_content,
                download_filename=f"procurement_spec_{clean_filename_base}.md"
            )
