from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class ClauseModel(BaseModel):
    clause_number: str
    clause_title: str
    content: str

class StandardCatalogItem(BaseModel):
    is_code: str
    base_code: str
    part: Optional[str] = None
    title: str
    publication_year: int
    reaffirmed_year: Optional[int] = None
    edition: Optional[str] = None
    division_code: str
    division_name: str
    sectional_committee: Optional[str] = None
    status: str
    supersedes: List[str] = Field(default_factory=list)
    superseded_by: Optional[str] = None
    mandatory_qco: bool = False
    qco_ministry: Optional[str] = None
    qco_order_name: Optional[str] = None
    scope: str
    keywords: List[str] = Field(default_factory=list)
    clauses: List[ClauseModel] = Field(default_factory=list)

class SpecificationAnalysisRequest(BaseModel):
    specification_text: str = Field(..., min_length=10, description="Raw procurement specifications or tender text")
    department_hint: Optional[str] = Field(None, description="Optional department hint: Civil, Electrical, Mechanical, Safety, Chemical")
    tender_reference: Optional[str] = Field(None, description="Optional tender notice / reference number")

class PhysicalDimension(BaseModel):
    parameter_name: str
    value: str
    tolerance: Optional[str] = None

class ExtractedParameters(BaseModel):
    commodity_name: str = Field(..., description="Identified core commodity / equipment")
    material_grade: Optional[str] = Field(None, description="Material grade or metallurgical alloy")
    intended_application: Optional[str] = Field(None, description="Target application or context")
    physical_dimensions: List[PhysicalDimension] = Field(default_factory=list)
    electrical_ratings: List[str] = Field(default_factory=list)
    mechanical_ratings: List[str] = Field(default_factory=list)
    testing_requirements: List[str] = Field(default_factory=list)
    detected_standard_citations: List[str] = Field(default_factory=list, description="Explicit standards already cited in text")
    detected_brands: List[str] = Field(default_factory=list, description="Brand or manufacturer names detected")

class BiasViolation(BaseModel):
    violation_id: str
    type: str  # BRAND_NAME_BIAS, MISSING_EQUIVALENCE, SUPERSEDED_STANDARD, FOREIGN_STANDARD_BIAS
    severity: str  # CRITICAL, WARNING, INFO
    offending_text: str
    gfr_rule: str  # e.g., Rule 144(i)(b)
    explanation: str
    suggested_replacement: str

class ComplianceAuditResult(BaseModel):
    health_score: int = Field(..., ge=0, le=100, description="Compliance Health Score (0-100)")
    is_gfr_compliant: bool
    is_qco_mandatory: bool
    qco_order_title: Optional[str] = None
    qco_ministry: Optional[str] = None
    violations_count: int
    violations: List[BiasViolation] = Field(default_factory=list)
    mandatory_clauses_to_insert: List[str] = Field(default_factory=list)

class ClauseCitation(BaseModel):
    clause_number: str
    clause_title: str
    alignment_reason: str
    standard_text_snippet: str

class StandardRecommendation(BaseModel):
    is_code: str
    base_code: str
    title: str
    publication_year: int
    reaffirmed_year: Optional[int] = None
    division_name: str
    status: str
    match_score: float = Field(..., ge=0, le=100)
    match_confidence: str  # HIGH, MEDIUM, LOW
    mandatory_qco: bool
    qco_ministry: Optional[str] = None
    superseded_warning: Optional[str] = None
    scope_summary: str
    clause_citations: List[ClauseCitation] = Field(default_factory=list)
    key_reasons: List[str] = Field(default_factory=list)

class AnalysisResponse(BaseModel):
    tender_reference: Optional[str] = None
    extracted_parameters: ExtractedParameters
    compliance_audit: ComplianceAuditResult
    recommendations: List[StandardRecommendation]
    sanitized_specification_text: str
    execution_time_ms: float

class ExportRequest(BaseModel):
    tender_title: str
    sanitized_text: str
    selected_standard: StandardRecommendation
    compliance_audit: ComplianceAuditResult
    export_format: str = "markdown"  # markdown, html, json

class ExportResponse(BaseModel):
    format: str
    content: str
    download_filename: str
