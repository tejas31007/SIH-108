# 06. Frontend Strategy & Stitch AI Integration Guide

## 1. What is Stitch AI and How It Fits Our Workflow

**Stitch AI** is an AI-powered design-to-code and rapid UI generation platform. It allows engineers to generate modern, production-grade frontend user interfaces from text prompts, design briefs, or wireframe descriptions, exporting clean, modular code (typically **React / Next.js with Tailwind CSS**).

### Our Workflow Strategy:
```
[Backend & AI Engine (FastAPI + RAG + Postgres)]
                       │
                       ▼ (Exposes REST API / OpenAPI JSON)
[Stitch AI: Prompt & Generate UI Screens]
                       │
                       ▼ (Export React + Tailwind Components)
[Integrate & Wire Components to FastAPI Endpoints]
                       │
                       ▼
[Complete Hackathon Demonstration Platform]
```

By leveraging Stitch AI for frontend development, we can achieve high-fidelity UI/UX (clean enterprise dashboard look, dark/light theme, interactive modals, responsive data tables) in a fraction of the time, allowing us to focus on the deep engineering challenges of NLP, RAG, and compliance logic.

---

## 2. Essential Screen Designs Required for SIH26108

To impress the hackathon judges and ministry officials, our UI must look like an enterprise-grade government portal (e.g., GeM / BIS Manakonline integrated tool).

### Screen 1: The Procurement Ingestion Hub
* **Components:**
  * Clean header with Ministry of Consumer Affairs & BIS branding.
  * Dual-mode input:
    1. **File Dropzone:** Upload RFP / Tender documents (PDF, DOCX).
    2. **Direct Text Editor:** Paste technical specification schedules or buyer ATC clauses.
  * Department & Category selector (e.g., Civil / Electrical / Mechanical / Safety).
  * "Run Intelligent Audit & Match" call-to-action button.

### Screen 2: Interactive Parameter & Compliance Audit Screen
* **Left Column: Extracted Technical Parameters**
  * Structured cards showing identified Commodity, Material Grades, Dimensions, and Performance Ratings.
  * Editable chips allowing the procurement officer to correct or add parameters (human-in-the-loop).
* **Right Column: GFR 144(i) Anti-Bias & QCO Audit Card**
  * **Overall Compliance Score Gauge** (e.g., `82/100`).
  * **Violations Alert Feed:**
    * 🔴 *Critical:* Direct brand name detected (`"Tata Tiscon"`). Button: `[Auto-Sanitize to Generic Text]`.
    * 🟡 *Warning:* Missing "or equivalent" clause.
    * 🟢 *Notice:* Subject to mandatory QCO (Ministry of Steel, 2018).

### Screen 3: Standards Recommendation & Evidence Deck
* **Top-Matched Indian Standards Cards:**
  * `IS 1786 : 2008` (94% Match) | `IS 432 : 1982` (68% Match) | `IS 2062 : 2011` (61% Match).
  * Status Pill: `ACTIVE` / `SUPERSEDED` / `MANDATORY QCO`.
* **Clause-Level Evidence Drawer:**
  * When a standard is clicked, show side-by-side matching clauses:
    * Tender requirement: `Yield stress 500 MPa` $\longleftrightarrow$ IS 1786 Clause 4.2 & Table 3.
* **Decision Controls:** `[Accept Standard]`, `[Reject]`, `[Add Custom Clause]`.

### Screen 4: One-Click Export & GeM Specification Sheet
* Generates an audit-ready, standardized procurement schedule.
* Formats: PDF tender annexure, Word document, or GeM-compatible JSON payload.

---

## 3. Stitch AI Prompting Playbook

When using Stitch AI, prompt with high precision using the following tailored templates:

### Prompt 1: Dashboard & Ingestion Interface
> *"Design a modern, clean enterprise web dashboard for the Bureau of Indian Standards (BIS) and Government e-Marketplace (GeM). Theme: Clean slate/blue government modern palette, Lucide icons, Tailwind CSS. Include a header with breadcrumbs and user profile. The main content has two columns: Left column features a drag-and-drop file upload zone for tender PDFs and an expandable text area for pasting procurement specifications. Right column features quick guidelines for GFR 144(i) procurement rules and a recent audits table with status badges (Approved, Flagged, Pending Review). Add a primary action button 'Analyze & Match Standards'."*

### Prompt 2: Standards Recommendation & Comparison Deck
> *"Create a responsive React component for displaying AI-recommended Indian Standards. Each standard is shown as a high-density card featuring: IS standard code (e.g., 'IS 1786:2008'), standard title, match percentage bar with color gradient (green for >90%, orange for 70-89%), status badge ('ACTIVE', 'QCO MANDATORY', 'SUPERSEDED'), and an expandable section showing clause-level evidence matching the user's technical parameters. Provide 'Accept Standard' and 'View Details' buttons on each card."*

### Prompt 3: GFR 144(i) Anti-Bias Audit Panel
> *"Create an alert-driven compliance audit panel for public tenders. Display an overall Compliance Health Score meter (0-100). Below the meter, list categorized flagged issues: Red cards for Brand Name Violations with an 'Auto-Sanitize' button, Yellow cards for Missing 'Or Equivalent' clauses, and Blue cards for Mandatory Quality Control Orders (QCO) alerts. Include a diff view showing the original biased text versus the sanitized neutral specification text."*

---

## 4. Integrating Stitch AI Code with our FastAPI Backend

### Step-by-Step Integration Guide

```
1. Generate screens in Stitch AI using our prompt templates.
2. Export React / Tailwind components into our `frontend/src/components/` folder.
3. Define TypeScript interfaces matching the FastAPI backend response schemas.
4. Use standard fetch / Axios hooks to communicate with FastAPI endpoints.
```

### Backend API Contracts to Connect:

#### 1. Ingestion & Analysis Endpoint
* **`POST /api/v1/analyze-specification`**
  * **Payload:** `{ "text": "...", "department": "Civil" }` or `multipart/form-data` with PDF file.
  * **Response:**
```json
{
  "extracted_parameters": {
    "commodity": "High Strength Deformed Steel Bars",
    "grade": "Fe 500D",
    "dimensions": ["12mm", "16mm"],
    "yield_strength": "500 MPa"
  },
  "compliance_audit": {
    "health_score": 75,
    "violations": [
      {
        "type": "BRAND_NAME_BIAS",
        "snippet": "Tata Tiscon 500D",
        "suggestion": "Fe 500D conforming to IS 1786"
      }
    ],
    "is_qco_mandatory": true,
    "qco_details": "Ministry of Steel Order 2018"
  },
  "recommendations": [
    {
      "is_code": "IS 1786:2008",
      "title": "High Strength Deformed Steel Bars and Wires for Concrete Reinforcement",
      "confidence": 94.5,
      "status": "ACTIVE",
      "clause_citations": [
        "Clause 4.2 (Fe 500D Grade Specification)",
        "Table 3 (Mechanical Properties: Min 500 MPa 0.2% Proof Stress)"
      ]
    }
  ]
}
```

#### 2. Sanitize & Export Endpoint
* **`POST /api/v1/export-specification`**
  * Generates the sanitized tender document in PDF/DOCX format ready for GeM upload.
