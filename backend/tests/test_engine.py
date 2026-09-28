import sys
from pathlib import Path

# Ensure root directory is in sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT_DIR))

from backend.config import SAMPLE_TENDERS_DIR
from backend.services.parser_service import ParserService
from backend.services.nlp_extractor import NLPExtractor
from backend.services.anti_bias_service import AntiBiasService
from backend.services.hybrid_retriever import HybridRetriever
from backend.services.compliance_service import ComplianceService
from backend.services.export_service import ExportService
from backend.models.schemas import ExportRequest, SpecificationAnalysisRequest
from backend.main import analyze_specification

def test_steel_rebars_tender():
    print("\n--- Running Test 1: Steel Rebars Tender ---")
    tender_file = SAMPLE_TENDERS_DIR / "tender_steel_rebars.txt"
    with open(tender_file, "r", encoding="utf-8") as f:
        tender_text = f.read()

    req = SpecificationAnalysisRequest(specification_text=tender_text, tender_reference="NIT/STEEL/2026/01")
    res = analyze_specification(req)

    print(f"Detected Commodity: {res.extracted_parameters.commodity_name}")
    print(f"Extracted Grade: {res.extracted_parameters.material_grade}")
    print(f"Mechanical Ratings: {res.extracted_parameters.mechanical_ratings}")
    print(f"Compliance Health Score: {res.compliance_audit.health_score}/100")
    print(f"Mandatory QCO in Force: {res.compliance_audit.is_qco_mandatory}")
    print(f"Top 1 Recommendation: {res.recommendations[0].is_code} - {res.recommendations[0].title}")
    print(f"Match Score: {res.recommendations[0].match_score}% ({res.recommendations[0].match_confidence})")
    
    # Assertions
    assert "IS 1786" in res.recommendations[0].is_code, "Expected IS 1786 to be top recommendation"
    assert res.compliance_audit.is_qco_mandatory is True, "Expected QCO to be mandatory for steel rebars"
    assert any("SUPERSEDED" in v.type for v in res.compliance_audit.violations), "Expected superseded IS 1139 alert"
    print(">>> Test 1 PASSED!")

def test_pvc_cables_brand_bias():
    print("\n--- Running Test 2: PVC Cables & Brand Bias Detection ---")
    tender_file = SAMPLE_TENDERS_DIR / "tender_pvc_cables.txt"
    with open(tender_file, "r", encoding="utf-8") as f:
        tender_text = f.read()

    req = SpecificationAnalysisRequest(specification_text=tender_text)
    res = analyze_specification(req)

    print(f"Detected Commodity: {res.extracted_parameters.commodity_name}")
    print(f"Electrical Ratings: {res.extracted_parameters.electrical_ratings}")
    print(f"Detected Brands: {res.extracted_parameters.detected_brands}")
    print(f"Compliance Health Score: {res.compliance_audit.health_score}/100")
    print(f"Top 1 Recommendation: {res.recommendations[0].is_code}")
    print(f"Violations Count: {res.compliance_audit.violations_count}")
    
    # Check that Havells brand was flagged
    brand_flags = [v for v in res.compliance_audit.violations if "Havells" in v.offending_text or v.type == "BRAND_NAME_BIAS"]
    print(f"Flagged Brand Violations: {len(brand_flags)}")
    
    # Check sanitized text
    print(f"Sanitized Text Preview:\n{res.sanitized_specification_text[-300:]}")

    # Assertions
    assert len(brand_flags) > 0, "Expected Havells brand violation to be flagged"
    assert "IS 694" in res.recommendations[0].is_code, "Expected IS 694 to be top recommendation for 1100V PVC cable"
    assert res.compliance_audit.is_qco_mandatory is True, "Expected mandatory QCO for cables"
    assert "Havells" not in res.sanitized_specification_text or "or equivalent" in res.sanitized_specification_text
    print(">>> Test 2 PASSED!")

def test_helmets_tender():
    print("\n--- Running Test 3: Industrial Helmets Tender ---")
    tender_file = SAMPLE_TENDERS_DIR / "tender_industrial_helmets.txt"
    with open(tender_file, "r", encoding="utf-8") as f:
        tender_text = f.read()

    req = SpecificationAnalysisRequest(specification_text=tender_text)
    res = analyze_specification(req)

    print(f"Detected Commodity: {res.extracted_parameters.commodity_name}")
    print(f"Testing Requirements: {res.extracted_parameters.testing_requirements}")
    print(f"Top 1 Recommendation: {res.recommendations[0].is_code} - {res.recommendations[0].title}")
    print(f"Mandatory QCO: {res.recommendations[0].mandatory_qco}")

    # Assertions
    assert "IS 2925" in res.recommendations[0].is_code, "Expected IS 2925 to be top recommendation for safety helmets"
    assert res.recommendations[0].mandatory_qco is True
    print(">>> Test 3 PASSED!")

def test_export_service():
    print("\n--- Running Test 4: Document Export Engine ---")
    tender_file = SAMPLE_TENDERS_DIR / "tender_steel_rebars.txt"
    with open(tender_file, "r", encoding="utf-8") as f:
        tender_text = f.read()

    req = SpecificationAnalysisRequest(specification_text=tender_text, tender_reference="FLYOVER-REBAR-2026")
    analysis = analyze_specification(req)

    export_req = ExportRequest(
        tender_title="Procurement of TMT Steel Reinforcement Bars",
        sanitized_text=analysis.sanitized_specification_text,
        selected_standard=analysis.recommendations[0],
        compliance_audit=analysis.compliance_audit,
        export_format="markdown"
    )

    export_res = ExportService.generate_export(export_req)
    assert export_res.format == "markdown"
    assert "IS 1786" in export_res.content
    assert "STATUTORY QUALITY MANDATE" in export_res.content
    print("Markdown Export verified.")

    export_req.export_format = "html"
    export_html = ExportService.generate_export(export_req)
    assert export_html.format == "html"
    assert "<!DOCTYPE html>" in export_html.content
    print("HTML Export verified.")

    export_req.export_format = "json"
    export_json = ExportService.generate_export(export_req)
    assert export_json.format == "json"
    assert "GeM_Compliant_Procurement_Specification" in export_json.content
    print("JSON Export verified.")
    print(">>> Test 4 PASSED!")

def test_food_fortified_rice():
    print("\n--- Running Test 5: Food & Public Distribution - Fortified Rice Kernels (FRK) ---")
    tender_file = SAMPLE_TENDERS_DIR / "tender_fortified_rice_frk.txt"
    with open(tender_file, "r", encoding="utf-8") as f:
        tender_text = f.read()

    req = SpecificationAnalysisRequest(specification_text=tender_text)
    res = analyze_specification(req)

    print(f"Detected Commodity: {res.extracted_parameters.commodity_name}")
    print(f"Ratings: {res.extracted_parameters.mechanical_ratings}")
    print(f"Top 1 Recommendation: {res.recommendations[0].is_code} - {res.recommendations[0].title}")
    print(f"Match Score: {res.recommendations[0].match_score}%")
    print(f"Aligned Clauses: {[c.clause_number for c in res.recommendations[0].clause_citations]}")

    assert "IS 17782" in res.recommendations[0].is_code, "Expected IS 17782 for Fortified Rice Kernels"
    print(">>> Test 5 PASSED!")

def test_food_pds_atta():
    print("\n--- Running Test 6: Food & Public Distribution - PDS Wheat Atta & Brand Bias ---")
    tender_file = SAMPLE_TENDERS_DIR / "tender_pds_wheat_atta.txt"
    with open(tender_file, "r", encoding="utf-8") as f:
        tender_text = f.read()

    req = SpecificationAnalysisRequest(specification_text=tender_text)
    res = analyze_specification(req)

    print(f"Detected Commodity: {res.extracted_parameters.commodity_name}")
    print(f"Detected Brands: {res.extracted_parameters.detected_brands}")
    print(f"Top 1 Recommendation: {res.recommendations[0].is_code} - {res.recommendations[0].title}")
    
    assert "IS 1155" in res.recommendations[0].is_code, "Expected IS 1155 for Wheat Atta"
    assert len(res.compliance_audit.violations) > 0, "Expected brand violations for Aashirvaad/Fortune Atta"
    assert "IS 1155" in res.sanitized_specification_text, "Expected sanitized text to cite IS 1155"
    print(">>> Test 6 PASSED!")

if __name__ == "__main__":
    print("==================================================")
    print("Starting BharatStandards AI Engine Verification Suite")
    print("==================================================")
    test_steel_rebars_tender()
    test_pvc_cables_brand_bias()
    test_helmets_tender()
    test_export_service()
    test_food_fortified_rice()
    test_food_pds_atta()
    print("\n==================================================")
    print("ALL 6 INTEGRATION TESTS PASSED SUCCESSFULLY! 100%")
    print("==================================================")

