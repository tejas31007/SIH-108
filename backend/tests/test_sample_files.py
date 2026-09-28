"""
Test suite to verify that sample_files (.pdf, .docx, .txt) parse cleanly and produce accurate recommendations.
"""
import sys
import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT_DIR))

from backend.services.parser_service import ParserService
from backend.services.nlp_extractor import NLPExtractor
from backend.services.anti_bias_service import AntiBiasService
from backend.services.hybrid_retriever import HybridRetriever
from backend.services.compliance_service import ComplianceService

nlp_extractor = NLPExtractor()
anti_bias_service = AntiBiasService()
hybrid_retriever = HybridRetriever()
compliance_service = ComplianceService()

SAMPLE_DIR = ROOT_DIR / "sample_files"

def run_pipeline(file_path: Path):
    with open(file_path, "rb") as f:
        file_bytes = f.read()
    
    extracted_text = ParserService.extract_text_from_bytes(file_bytes, file_path.name)
    assert len(extracted_text.strip()) > 50, f"Extracted text too short for {file_path.name}"
    
    isolated_text, detected_ref = ParserService.isolate_technical_sections(extracted_text)
    extracted_params = nlp_extractor.extract_parameters(isolated_text)
    compliance_audit = anti_bias_service.audit_specification(extracted_text)
    recommendations = hybrid_retriever.recommend(isolated_text, extracted_params, top_k=3)
    compliance_audit = compliance_service.verify_statutory_qco(compliance_audit, recommendations)
    
    return {
        "file": file_path.name,
        "ref": detected_ref,
        "top_standard": recommendations[0].is_code if recommendations else "None",
        "match_score": recommendations[0].match_score if recommendations else 0,
        "violations": compliance_audit.violations_count,
        "qco_mandatory": compliance_audit.is_qco_mandatory
    }

def main():
    print("Testing Sample Files across PDF, DOCX, and TXT formats...")
    
    test_files = [
        # PDF Tests
        ("01_food_fortified_rice_frk.pdf", "IS 17782"),
        ("03_food_jute_bags_50kg_fci.pdf", "IS 12650"),
        ("05_civil_flyover_tmt_rebars_obsolete_biased.pdf", "IS 1786"),
        ("07_civil_hdpe_water_pipes_jjm.pdf", "IS 4984"),
        ("10_safety_industrial_helmets_qco.pdf", "IS 2925"),
        # DOCX Tests
        ("02_food_pds_wheat_atta_biased.docx", "IS 1155"),
        ("06_civil_ppc_cement_biased.docx", "IS 1489 Part 1"),
        ("08_electrical_pvc_armoured_cables_biased.docx", "IS 1554 Part 1"),
        ("12_it_laptops_brand_biased_dell.docx", "IS 13252 Part 1"),
        # TXT Tests
        ("04_food_packaged_drinking_water_biased.txt", "IS 14543"),
        ("09_electrical_solar_grid_inverter.txt", "IS 16221 Part 2"),
        ("11_safety_n95_respiratory_masks.txt", "IS 9473"),
        ("13_mechanical_centrifugal_pump.txt", "IS 1520"),
        ("14_textiles_cotton_hospital_bedsheets.txt", "IS 745"),
    ]
    
    passed = 0
    for filename, expected_code in test_files:
        path = SAMPLE_DIR / filename
        assert path.exists(), f"File {filename} does not exist!"
        result = run_pipeline(path)
        print(f"[{result['file']}] -> Top: {result['top_standard']} (Score: {result['match_score']}%, Violations: {result['violations']}, QCO: {result['qco_mandatory']})")
        
        # Check standard match
        expected_base = expected_code.split()[0] + " " + expected_code.split()[1]
        assert expected_base in result["top_standard"], f"For {filename}: Expected {expected_code}, got {result['top_standard']}"
        passed += 1
        
    print(f"\nAll {passed}/{len(test_files)} sample files verified successfully!")

if __name__ == "__main__":
    main()
