import time
import json
from typing import Optional, List
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles

from backend.config import (
    APP_TITLE, APP_DESCRIPTION, APP_VERSION, CORS_ORIGINS,
    STANDARDS_CATALOG_PATH, QCO_REGISTRY_PATH, SUPERSEDED_MAPPING_PATH,
    STITCH_DIR
)
from backend.models.schemas import (
    SpecificationAnalysisRequest, AnalysisResponse,
    StandardCatalogItem, ExportRequest, ExportResponse
)
from backend.services.parser_service import ParserService
from backend.services.nlp_extractor import NLPExtractor
from backend.services.anti_bias_service import AntiBiasService
from backend.services.hybrid_retriever import HybridRetriever
from backend.services.compliance_service import ComplianceService
from backend.services.export_service import ExportService

# Initialize FastAPI application
app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION
)

# Mount static frontend directory if it exists
if STITCH_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STITCH_DIR), html=True), name="static")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Core AI & Compliance Services
nlp_extractor = NLPExtractor()
anti_bias_service = AntiBiasService()
hybrid_retriever = HybridRetriever()
compliance_service = ComplianceService()

@app.get("/")
def root(request: Request):
    dashboard_file = STITCH_DIR / "dashboard.html"
    if dashboard_file.exists():
        return FileResponse(dashboard_file)
    return {
        "status": "healthy",
        "service": APP_TITLE,
        "version": APP_VERSION,
        "standards_indexed": len(hybrid_retriever.standards),
        "docs_url": "/docs"
    }

@app.get("/api")
def api_info():
    return {
        "status": "healthy",
        "service": APP_TITLE,
        "version": APP_VERSION,
        "standards_indexed": len(hybrid_retriever.standards),
        "docs_url": "/docs"
    }

@app.get("/health")
def health_check():
    return {"status": "ok", "timestamp": time.time()}

@app.get("/api/v1/standards", response_model=List[StandardCatalogItem])
def list_standards(
    search: Optional[str] = Query(None, description="Keyword search in standards"),
    division: Optional[str] = Query(None, description="Filter by Division code: CED, ETD, etc.")
):
    """Retrieve catalog of Indian Standards with optional filtering."""
    results = hybrid_retriever.standards
    if division:
        results = [s for s in results if s.get("division_code", "").upper() == division.upper()]
    if search:
        s_lower = search.lower()
        results = [
            s for s in results 
            if s_lower in s.get("is_code", "").lower() 
            or s_lower in s.get("title", "").lower()
            or any(s_lower in kw.lower() for kw in s.get("keywords", []))
        ]
    return results

@app.get("/api/v1/qco-list")
def list_qco_orders():
    """Retrieve list of active Quality Control Orders."""
    return compliance_service.qco_records

@app.get("/api/v1/superseded-standards")
def list_superseded_standards():
    """Retrieve list of obsolete/superseded Indian Standards."""
    return anti_bias_service.superseded_data

@app.post("/api/v1/analyze", response_model=AnalysisResponse)
def analyze_specification(request: SpecificationAnalysisRequest):
    """Analyze raw procurement specification text and recommend applicable Indian Standards."""
    start_time = time.time()
    raw_text = request.specification_text

    # 1. Isolate Technical Sections
    isolated_text, detected_ref = ParserService.isolate_technical_sections(raw_text)
    tender_ref = request.tender_reference or detected_ref

    # 2. Extract Technical Parameters
    extracted_params = nlp_extractor.extract_parameters(isolated_text)

    # 3. Audit for GFR 144(i) Brand Bias & Superseded Standards
    compliance_audit = anti_bias_service.audit_specification(raw_text)

    # 4. Hybrid Standards Recommendation
    recommendations = hybrid_retriever.recommend(
        query_text=isolated_text,
        extracted=extracted_params,
        top_k=4
    )

    # 5. Verify Statutory QCO & Mandatory Certification
    compliance_audit = compliance_service.verify_statutory_qco(compliance_audit, recommendations)

    # 6. Auto-Sanitize Biased Text
    sanitized_text = anti_bias_service.sanitize_text(raw_text, compliance_audit)

    elapsed_ms = round((time.time() - start_time) * 1000, 2)

    return AnalysisResponse(
        tender_reference=tender_ref,
        extracted_parameters=extracted_params,
        compliance_audit=compliance_audit,
        recommendations=recommendations,
        sanitized_specification_text=sanitized_text,
        execution_time_ms=elapsed_ms
    )

@app.post("/api/v1/analyze-file", response_model=AnalysisResponse)
async def analyze_uploaded_file(
    file: UploadFile = File(...),
    department_hint: Optional[str] = Form(None),
    tender_reference: Optional[str] = Form(None)
):
    """Upload a tender document (PDF, DOCX, TXT) and run automated standards recommendation."""
    start_time = time.time()
    file_bytes = await file.read()
    
    if len(file_bytes) == 0:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    extracted_text = ParserService.extract_text_from_bytes(file_bytes, file.filename)
    if len(extracted_text.strip()) < 10:
        raise HTTPException(status_code=400, detail="Could not extract readable text from document.")

    # 1. Isolate Technical Section
    isolated_text, detected_ref = ParserService.isolate_technical_sections(extracted_text)
    tender_ref = tender_reference or detected_ref or file.filename

    # 2. NLP Parameter Extraction
    extracted_params = nlp_extractor.extract_parameters(isolated_text)

    # 3. GFR 144(i) Anti-Bias Audit
    compliance_audit = anti_bias_service.audit_specification(extracted_text)

    # 4. Hybrid Recommendations
    recommendations = hybrid_retriever.recommend(
        query_text=isolated_text,
        extracted=extracted_params,
        top_k=4
    )

    # 5. QCO Compliance Verification
    compliance_audit = compliance_service.verify_statutory_qco(compliance_audit, recommendations)

    # 6. Auto-Sanitization
    sanitized_text = anti_bias_service.sanitize_text(extracted_text, compliance_audit)

    elapsed_ms = round((time.time() - start_time) * 1000, 2)

    return AnalysisResponse(
        tender_reference=tender_ref,
        extracted_parameters=extracted_params,
        compliance_audit=compliance_audit,
        recommendations=recommendations,
        sanitized_specification_text=sanitized_text,
        execution_time_ms=elapsed_ms
    )

@app.post("/api/v1/export", response_model=ExportResponse)
def export_specification(request: ExportRequest):
    """Generate GeM-compliant procurement specification document in Markdown, HTML, or JSON."""
    return ExportService.generate_export(request)
