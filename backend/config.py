import os
from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Data file paths
STANDARDS_CATALOG_PATH = DATA_DIR / "standards_catalog.json"
QCO_REGISTRY_PATH = DATA_DIR / "qco_registry.json"
SUPERSEDED_MAPPING_PATH = DATA_DIR / "superseded_mapping.json"
BRANDS_GAZETTEER_PATH = DATA_DIR / "brands_gazetteer.json"
SAMPLE_TENDERS_DIR = DATA_DIR / "sample_tenders"
STITCH_DIR = BASE_DIR / "stitchAI"

# Application Settings
APP_TITLE = "BharatStandards AI - Indian Standards Recommendation Engine"
APP_DESCRIPTION = (
    "AI-Powered Recommendation Engine for Identifying Applicable Indian Standards "
    "for Public Procurement Specifications (SIH26108 / Ministry of Consumer Affairs)"
)
APP_VERSION = "1.0.0"

# CORS configuration
CORS_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
    "*"
]
