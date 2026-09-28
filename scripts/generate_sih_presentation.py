"""
Generates the official Smart India Hackathon (SIH 2026) Round 1 Presentation Deck
for Problem Statement SIH26108:
"AI-Powered Recommendation Engine for Identifying Applicable Indian Standards for Procurement Specifications"
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "presentation"))
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "SIH26108_BharatStandards_AI_Round1_Presentation.pptx")

# -------------------------------------------------------------
# Color Palette & Styling Constants
# -------------------------------------------------------------
NAVY_DARK = RGBColor(12, 28, 62)       # Primary Dark Navy #0C1C3E
NAVY_LIGHT = RGBColor(22, 48, 102)     # Secondary Navy
SAFFRON = RGBColor(230, 95, 20)        # Saffron Accent #E65F14
GOLD = RGBColor(245, 158, 11)          # Amber Gold #F59E0B
SLATE_DARK = RGBColor(30, 41, 59)      # Body Text #1E293B
SLATE_MUTED = RGBColor(100, 116, 139)  # Subtitles/Muted #64748B
BG_LIGHT = RGBColor(248, 250, 252)     # Slide Background #F8FAFC
CARD_BG = RGBColor(255, 255, 255)      # Card White
CARD_BORDER = RGBColor(226, 232, 240)  # Card Border #E2E8F0
CARD_MUTED_BG = RGBColor(241, 245, 249) # Subcard #F1F5F9
EMERALD = RGBColor(16, 149, 93)        # Green Success/Compliance
RED_ACCENT = RGBColor(220, 38, 38)     # Red Warning
WHITE = RGBColor(255, 255, 255)

FONT_HEADING = "Segoe UI"
FONT_BODY = "Segoe UI"

def set_slide_background(slide, color):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_header(slide, category_text: str, title_text: str):
    """Adds a standard executive header to content slides."""
    # Top Category Pill / Bar
    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
    tf_cat = cat_box.text_frame
    tf_cat.word_wrap = True
    tf_cat.margin_left = tf_cat.margin_right = tf_cat.margin_top = tf_cat.margin_bottom = 0
    p_cat = tf_cat.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.name = FONT_HEADING
    p_cat.font.size = Pt(10)
    p_cat.font.bold = True
    p_cat.font.color.rgb = SAFFRON
    
    # Main Title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.55))
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    tf_title.margin_left = tf_title.margin_right = tf_title.margin_top = tf_title.margin_bottom = 0
    p_title = tf_title.paragraphs[0]
    p_title.text = title_text
    p_title.font.name = FONT_HEADING
    p_title.font.size = Pt(20)
    p_title.font.bold = True
    p_title.font.color.rgb = NAVY_DARK

    # Subtle divider line
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.35), Inches(11.73), Inches(0.02))
    line.fill.solid()
    line.fill.fore_color.rgb = CARD_BORDER
    line.line.color.rgb = CARD_BORDER

def create_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
    """Creates a clean card shape with subtle border."""
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(1)
    else:
        card.line.fill.background()
    return card

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # =========================================================================
    # SLIDE 1: Title Slide (Dark Navy Executive Presentation)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, NAVY_DARK)

    # Decorative saffron top strip
    strip = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12))
    strip.fill.solid()
    strip.fill.fore_color.rgb = SAFFRON
    strip.line.fill.background()

    # SIH Header Badge
    badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(0.8), Inches(4.5), Inches(0.4))
    badge.fill.solid()
    badge.fill.fore_color.rgb = NAVY_LIGHT
    badge.line.color.rgb = SAFFRON
    badge.line.width = Pt(1)
    tf_b = badge.text_frame
    tf_b.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_b = tf_b.paragraphs[0]
    p_b.text = "SMART INDIA HACKATHON 2026 | ROUND 1 EVALUATION"
    p_b.font.name = FONT_HEADING
    p_b.font.size = Pt(10)
    p_b.font.bold = True
    p_b.font.color.rgb = WHITE
    p_b.alignment = PP_ALIGN.CENTER

    # Problem Statement ID & Ministry
    ps_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.4), Inches(11.3), Inches(0.6))
    tf_ps = ps_box.text_frame
    p_ps = tf_ps.paragraphs[0]
    p_ps.text = "PROBLEM STATEMENT ID: SIH26108  •  SOFTWARE EDITION"
    p_ps.font.name = FONT_HEADING
    p_ps.font.size = Pt(12)
    p_ps.font.bold = True
    p_ps.font.color.rgb = SAFFRON

    p_min = tf_ps.add_paragraph()
    p_min.text = "Ministry of Consumer Affairs, Food & Public Distribution | Bureau of Indian Standards (BIS)"
    p_min.font.name = FONT_HEADING
    p_min.font.size = Pt(11)
    p_min.font.color.rgb = RGBColor(190, 205, 230)

    # Main Project Title
    title_box = s1.shapes.add_textbox(Inches(1.0), Inches(2.3), Inches(11.3), Inches(1.8))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = "BharatStandards AI"
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(36)
    p_t.font.bold = True
    p_t.font.color.rgb = WHITE

    p_sub = tf_t.add_paragraph()
    p_sub.text = "An Intelligent NLP & Hybrid Retrieval Engine for Identifying Applicable Indian Standards, Auditing GFR 144(i) Bias, and Enforcing Statutory QCOs in Public Procurement"
    p_sub.font.name = FONT_BODY
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = RGBColor(215, 225, 245)
    p_sub.space_before = Pt(8)

    # Key Highlights Badges
    badges = [
        "✓ Clause-Level Precision (Table & Citations)",
        "✓ Automated GFR 144(i) Anti-Bias Audit",
        "✓ Statutory QCO & Mandatory ISI Enforcement",
        "✓ GeM-Ready Procurement Schedule Generator"
    ]
    for idx, badge_text in enumerate(badges):
        bx = Inches(1.0 + (idx * 2.85))
        card = create_card(s1, bx, Inches(4.3), Inches(2.75), Inches(0.65), bg_color=NAVY_LIGHT, border_color=SAFFRON)
        tf_card = card.text_frame
        tf_card.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf_card.paragraphs[0]
        p.text = badge_text
        p.font.name = FONT_HEADING
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p.alignment = PP_ALIGN.CENTER

    # Team & Submission Details Card
    t_card = create_card(s1, Inches(1.0), Inches(5.3), Inches(11.33), Inches(1.4), bg_color=NAVY_LIGHT, border_color=CARD_BORDER)
    tf_tc = t_card.text_frame
    tf_tc.margin_left = Inches(0.3)
    tf_tc.margin_top = Inches(0.2)
    p_tc1 = tf_tc.paragraphs[0]
    p_tc1.text = "PROPOSED BY: TEAM INNOVATORS  |  INSTITUTE: SMART INDIA HACKATHON PARTICIPATING TEAM"
    p_tc1.font.name = FONT_HEADING
    p_tc1.font.size = Pt(11)
    p_tc1.font.bold = True
    p_tc1.font.color.rgb = SAFFRON

    p_tc2 = tf_tc.add_paragraph()
    p_tc2.text = "Team Leader: [Candidate / Lead Engineer]  •  Focus Area: Natural Language Processing, Regulatory AI & Public Policy"
    p_tc2.font.name = FONT_BODY
    p_tc2.font.size = Pt(10)
    p_tc2.font.color.rgb = WHITE
    p_tc2.space_before = Pt(4)

    p_tc3 = tf_tc.add_paragraph()
    p_tc3.text = "Submission Category: Software | Track: Smart Automation / Governance & Citizen Welfare | Hackathon Edition: SIH 2026"
    p_tc3.font.name = FONT_BODY
    p_tc3.font.size = Pt(9.5)
    p_tc3.font.color.rgb = RGBColor(180, 195, 220)
    p_tc3.space_before = Pt(3)

    # =========================================================================
    # SLIDE 2: Context & Ground Reality (The Procurement Challenge)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, BG_LIGHT)
    add_header(s2, "Context & Ground Problem", "Challenges in Indian Public Procurement Specifications")

    # Executive Context Banner
    ctx_box = create_card(s2, Inches(0.8), Inches(1.5), Inches(11.73), Inches(0.8), bg_color=RGBColor(238, 242, 255), border_color=RGBColor(199, 210, 254))
    tf_ctx = ctx_box.text_frame
    tf_ctx.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_ctx.margin_left = Inches(0.3)
    p_ctx = tf_ctx.paragraphs[0]
    p_ctx.text = "The Ground Reality: Over ₹15 Lakh Crore worth of public procurement is processed annually across GeM and CPPP. Yet, government tender drafting is manual, fragmented, and vulnerable to anti-competitive bias and quality lapses."
    p_ctx.font.name = FONT_BODY
    p_ctx.font.size = Pt(11)
    p_ctx.font.color.rgb = NAVY_DARK
    p_ctx.font.bold = True

    # 4 Pain Points in 2x2 Grid
    pain_points = [
        {
            "num": "01",
            "title": "Heterogeneous & Ambiguous Drafting",
            "tag": "STANDARDIZATION DEFICIT",
            "tag_color": RED_ACCENT,
            "desc": "Tender drafting officers across 1,000+ departments write specifications in informal, proprietary, or ambiguous formats without standardized parameters or direct citations of Bureau of Indian Standards (BIS)."
        },
        {
            "num": "02",
            "title": "Unlawful Brand Name Bias",
            "tag": "GFR 2017 RULE 144(i) VIOLATION",
            "tag_color": RED_ACCENT,
            "desc": "Tenders routinely specify restrictive proprietary brand names (e.g., 'Tata Tiscon', 'Havells', 'Aashirvaad') without adding 'or equivalent', creating unlawful single-vendor lock-ins and violating open competition."
        },
        {
            "num": "03",
            "title": "Citation of Obsolete / Superseded Standards",
            "tag": "LEGAL & QUALITY RISK",
            "tag_color": SAFFRON,
            "desc": "Procurement documents frequently cite deprecated or withdrawn standards (e.g. IS 1139:1966 instead of IS 1786:2008, or IS 8112 instead of IS 269), leading to tender cancellations, audit objections, and disputes."
        },
        {
            "num": "04",
            "title": "Overlooking Mandatory Quality Control Orders (QCOs)",
            "tag": "STATUTORY NON-COMPLIANCE",
            "tag_color": SAFFRON,
            "desc": "Central Ministries notify mandatory QCOs under the BIS Act 2016 making the ISI mark legally compulsory. Procurement officers often miss these statutory orders, allowing substandard non-certified goods into national infrastructure."
        }
    ]

    for idx, pp in enumerate(pain_points):
        row = idx // 2
        col = idx % 2
        x = Inches(0.8 + (col * 5.95))
        y = Inches(2.45 + (row * 2.35))
        
        card = create_card(s2, x, y, Inches(5.78), Inches(2.15), bg_color=CARD_BG, border_color=CARD_BORDER)
        tf = card.text_frame
        tf.margin_left = Inches(0.25)
        tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.2)

        p1 = tf.paragraphs[0]
        p1.text = f"{pp['num']}  •  {pp['tag']}"
        p1.font.name = FONT_HEADING
        p1.font.size = Pt(9.5)
        p1.font.bold = True
        p1.font.color.rgb = pp['tag_color']

        p2 = tf.add_paragraph()
        p2.text = pp['title']
        p2.font.name = FONT_HEADING
        p2.font.size = Pt(13)
        p2.font.bold = True
        p2.font.color.rgb = NAVY_DARK
        p2.space_before = Pt(3)

        p3 = tf.add_paragraph()
        p3.text = pp['desc']
        p3.font.name = FONT_BODY
        p3.font.size = Pt(10)
        p3.font.color.rgb = SLATE_DARK
        p3.space_before = Pt(5)

    # =========================================================================
    # SLIDE 3: Proposed Solution - "BharatStandards AI"
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, BG_LIGHT)
    add_header(s3, "Proposed Solution", "BharatStandards AI: An End-to-End Regulatory Recommendation Engine")

    # Solution Proposition Box
    prop_box = create_card(s3, Inches(0.8), Inches(1.5), Inches(11.73), Inches(0.95), bg_color=NAVY_DARK, border_color=SAFFRON)
    tf_prop = prop_box.text_frame
    tf_prop.margin_left = Inches(0.3)
    tf_prop.margin_top = Inches(0.15)
    p_pr1 = tf_prop.paragraphs[0]
    p_pr1.text = "CORE MISSION & INNOVATION:"
    p_pr1.font.name = FONT_HEADING
    p_pr1.font.size = Pt(10)
    p_pr1.font.bold = True
    p_pr1.font.color.rgb = SAFFRON

    p_pr2 = tf_prop.add_paragraph()
    p_pr2.text = "A purpose-built, explainable AI platform that converts raw, unstructured tender specifications (PDF, Word, or Text) into standardized, legally compliant procurement schedules citing the exact applicable Indian Standards with clause-level citations."
    p_pr2.font.name = FONT_BODY
    p_pr2.font.size = Pt(11)
    p_pr2.font.color.rgb = WHITE
    p_pr2.space_before = Pt(2)

    # 3 Solution Columns
    sol_columns = [
        {
            "icon": "📥",
            "title": "1. Multi-Format Ingestion & Isolation",
            "subtitle": "Document Processing Layer",
            "points": [
                "Ingests PDF, DOCX, and raw specification text.",
                "Extracts technical parameters while intelligently filtering out contractual and financial boilerplate.",
                "Isolates physical dimensions, grades, electrical ratings, mechanical strengths, and test criteria."
            ]
        },
        {
            "icon": "🧠",
            "title": "2. Hybrid Semantic-Lexical Engine",
            "subtitle": "AI Retrieval & Matching Layer",
            "points": [
                "Dual-scoring engine: BM25 lexical term matching + TF-IDF semantic cosine similarity.",
                "Domain-specific parameter boosting for exact material grade and physical attribute alignment.",
                "Clause-level matching: Pinpoints specific testing clauses and tables (e.g. Table 3 Proof Stress, Clause 9.2 Elongation)."
            ]
        },
        {
            "icon": "⚖️",
            "title": "3. Anti-Bias & Statutory QCO Enforcement",
            "subtitle": "Compliance & De-Biasing Layer",
            "points": [
                "Audits against GFR 2017 Rule 144(i) to detect commercial brand bias and proprietary vendor favoritism.",
                "Detects superseded / obsolete standards and provides active Gazette-backed replacements.",
                "Verifies mandatory Quality Control Orders (QCOs) from Central Ministries (DPIIT, Steel, MeitY, Power).",
                "Auto-generates clean, sanitized GeM procurement schedules with mandatory statutory compliance clauses."
            ]
        }
    ]

    for idx, col in enumerate(sol_columns):
        x = Inches(0.8 + (idx * 3.98))
        card = create_card(s3, x, Inches(2.65), Inches(3.8), Inches(4.3), bg_color=CARD_BG, border_color=CARD_BORDER)
        tf = card.text_frame
        tf.margin_left = Inches(0.25)
        tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.25)

        p0 = tf.paragraphs[0]
        p0.text = col['subtitle'].upper()
        p0.font.name = FONT_HEADING
        p0.font.size = Pt(9)
        p0.font.bold = True
        p0.font.color.rgb = SAFFRON

        p1 = tf.add_paragraph()
        p1.text = f"{col['icon']} {col['title']}"
        p1.font.name = FONT_HEADING
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = NAVY_DARK
        p1.space_before = Pt(3)

        # Subtle divider
        p_div = tf.add_paragraph()
        p_div.text = "—" * 28
        p_div.font.size = Pt(8)
        p_div.font.color.rgb = CARD_BORDER
        p_div.space_before = Pt(2)

        for pt in col['points']:
            p_pt = tf.add_paragraph()
            p_pt.text = f"• {pt}"
            p_pt.font.name = FONT_BODY
            p_pt.font.size = Pt(10)
            p_pt.font.color.rgb = SLATE_DARK
            p_pt.space_before = Pt(6)

    # =========================================================================
    # SLIDE 4: Proposed Architecture & Data Flow Pipeline
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, BG_LIGHT)
    add_header(s4, "System Architecture & Data Flow", "5-Stage Intelligent Processing & Recommendation Pipeline")

    stages = [
        {
            "stage": "STAGE 01",
            "name": "Document Ingestion & Isolation",
            "tech": "PyMuPDF • python-docx • Boundary RegEx",
            "desc": "Accepts PDF tenders, Word specs, and text. Isolates technical requirement sections; filters contractual terms & EMD clauses."
        },
        {
            "stage": "STAGE 02",
            "name": "Domain NLP Parameter Extraction",
            "tech": "Custom NER • Parameter Regex • Tokenizer",
            "desc": "Extracts commodity type, material grades (e.g. Fe 500D, PE 100), dimensions (OD, mm), mechanical/electrical ratings, and test criteria."
        },
        {
            "stage": "STAGE 03",
            "name": "Hybrid Lexical & Semantic Retrieval",
            "tech": "BM25 (Rank-BM25) • TF-IDF • Cosine Similarity",
            "desc": "Dual-index retrieval: BM25 ranks exact keyword hits; TF-IDF calculates semantic vector similarity. Parameter boosting matches exact grades."
        },
        {
            "stage": "STAGE 04",
            "name": "Anti-Bias & Statutory QCO Audit",
            "tech": "Brand Gazetteer • QCO Registry • Supersession DB",
            "desc": "Audits GFR 144(i) brand bias. Detects obsolete standards (e.g. IS 1139 -> IS 1786). Flags mandatory Quality Control Orders."
        },
        {
            "stage": "STAGE 05",
            "name": "Sanitization & GeM Bid Schedule Export",
            "tech": "Auto-Rewriter • Export Engine (MD / HTML / JSON)",
            "desc": "Rewrites biased tenders to generic functional specifications ('or equivalent'). Generates ready-to-publish GeM procurement schedules."
        }
    ]

    for idx, st in enumerate(stages):
        x = Inches(0.8 + (idx * 2.38))
        card = create_card(s4, x, Inches(1.6), Inches(2.28), Inches(4.5), bg_color=CARD_BG, border_color=CARD_BORDER)
        tf = card.text_frame
        tf.margin_left = Inches(0.18)
        tf.margin_right = Inches(0.18)
        tf.margin_top = Inches(0.2)

        # Stage Pill
        p_st = tf.paragraphs[0]
        p_st.text = st['stage']
        p_st.font.name = FONT_HEADING
        p_st.font.size = Pt(9.5)
        p_st.font.bold = True
        p_st.font.color.rgb = SAFFRON

        # Name
        p_nm = tf.add_paragraph()
        p_nm.text = st['name']
        p_nm.font.name = FONT_HEADING
        p_nm.font.size = Pt(11)
        p_nm.font.bold = True
        p_nm.font.color.rgb = NAVY_DARK
        p_nm.space_before = Pt(4)

        # Tech Badge Box
        p_tech = tf.add_paragraph()
        p_tech.text = st['tech']
        p_tech.font.name = FONT_HEADING
        p_tech.font.size = Pt(8)
        p_tech.font.bold = True
        p_tech.font.color.rgb = NAVY_LIGHT
        p_tech.space_before = Pt(8)

        # Description
        p_desc = tf.add_paragraph()
        p_desc.text = st['desc']
        p_desc.font.name = FONT_BODY
        p_desc.font.size = Pt(9.5)
        p_desc.font.color.rgb = SLATE_DARK
        p_desc.space_before = Pt(8)

    # Bottom Architectural Note
    arch_note = create_card(s4, Inches(0.8), Inches(6.25), Inches(11.73), Inches(0.7), bg_color=RGBColor(240, 253, 244), border_color=RGBColor(187, 247, 208))
    tf_an = arch_note.text_frame
    tf_an.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_an.margin_left = Inches(0.25)
    p_an = tf_an.paragraphs[0]
    p_an.text = "Key Architectural Feature: Explainable, Deterministic & Fast. The pipeline relies on verifiable lexical-semantic ranking with clause citations rather than opaque black-box LLM hallucinations, ensuring 100% legal defensibility in public audit."
    p_an.font.name = FONT_BODY
    p_an.font.size = Pt(9.5)
    p_an.font.bold = True
    p_an.font.color.rgb = RGBColor(22, 101, 52)

    # =========================================================================
    # SLIDE 5: Technology Stack & Justification
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, BG_LIGHT)
    add_header(s5, "Technology Stack & Justification", "Lightweight, Production-Ready, and Explainable Technologies")

    tech_categories = [
        {
            "category": "BACKEND & API SERVICES",
            "tech": "Python 3.14 & FastAPI",
            "badge": "HIGH PERFORMANCE REST API",
            "points": [
                "FastAPI asynchronous architecture delivers sub-50ms endpoint latencies.",
                "Auto-generated OpenAPI 3.0 (Swagger) documentation for plug-and-play GeM integration.",
                "Pydantic strict schema validation ensures rock-solid data integrity.",
                "Runs on minimal hardware resources (deployable on NIC Cloud / MeghRaj without expensive GPU clusters)."
            ]
        },
        {
            "category": "NLP & RETRIEVAL ENGINE",
            "tech": "Rank-BM25 & Scikit-Learn TF-IDF",
            "badge": "HYBRID SEARCH ARCHITECTURE",
            "points": [
                "BM25 Okapi Algorithm: Guarantees precise keyword matching on exact technical nomenclature and grades.",
                "TF-IDF Semantic Vectorizer: Handles synonymy and semantic re-ranking across domain vocabularies.",
                "Parameter Boosting Heuristic: Dynamically elevates standards matching exact physical & electrical attributes.",
                "100% Explainable scoring without non-deterministic hallucinations."
            ]
        },
        {
            "category": "USER EXPERIENCE & PORTAL",
            "tech": "Tailwind CSS & Modern JavaScript",
            "badge": "GOVERNMENT READY UI/UX",
            "points": [
                "Clean, accessible UI designed for public procurement officers without technical background.",
                "Drag-and-drop document upload for instant analysis of PDF, Word (.docx), and text files.",
                "Side-by-side sanitization diff visualizer showing exact GFR 144(i) corrections in red/green.",
                "One-click export of GeM tender schedules in Markdown, HTML, and JSON."
            ]
        },
        {
            "category": "STANDARDS KNOWLEDGE BASE",
            "tech": "BIS & Gazette Data Registry",
            "badge": "CURATED REGULATORY CORPUS",
            "points": [
                "Covers all 14 BIS Division Councils (Civil, Food, Electrical, Mechanical, IT, Safety, Textiles, etc.).",
                "Clause-level citation registry mapping testing protocols, dimensions, and limits.",
                "Active statutory Quality Control Orders (QCO) gazette registry from DPIIT, Steel, MeitY, and Power.",
                "Historical superseded standards mapping for auto-upgrading deprecated codes."
            ]
        }
    ]

    for idx, tc in enumerate(tech_categories):
        x = Inches(0.8 + (idx * 2.98))
        card = create_card(s5, x, Inches(1.5), Inches(2.82), Inches(5.4), bg_color=CARD_BG, border_color=CARD_BORDER)
        tf = card.text_frame
        tf.margin_left = Inches(0.2)
        tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.2)

        p_cat = tf.paragraphs[0]
        p_cat.text = tc['category']
        p_cat.font.name = FONT_HEADING
        p_cat.font.size = Pt(8.5)
        p_cat.font.bold = True
        p_cat.font.color.rgb = SAFFRON

        p_t = tf.add_paragraph()
        p_t.text = tc['tech']
        p_t.font.name = FONT_HEADING
        p_t.font.size = Pt(12)
        p_t.font.bold = True
        p_t.font.color.rgb = NAVY_DARK
        p_t.space_before = Pt(3)

        p_b = tf.add_paragraph()
        p_b.text = tc['badge']
        p_b.font.name = FONT_HEADING
        p_b.font.size = Pt(7.5)
        p_b.font.bold = True
        p_b.font.color.rgb = EMERALD
        p_b.space_before = Pt(2)

        p_div = tf.add_paragraph()
        p_div.text = "—" * 22
        p_div.font.size = Pt(8)
        p_div.font.color.rgb = CARD_BORDER
        p_div.space_before = Pt(2)

        for pt in tc['points']:
            p_pt = tf.add_paragraph()
            p_pt.text = f"• {pt}"
            p_pt.font.name = FONT_BODY
            p_pt.font.size = Pt(9.5)
            p_pt.font.color.rgb = SLATE_DARK
            p_pt.space_before = Pt(5)

    # =========================================================================
    # SLIDE 6: Innovation & Unique Selling Propositions (USPs)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, BG_LIGHT)
    add_header(s6, "Innovation & Key USPs", "What Sets BharatStandards AI Apart From Generic AI Solutions")

    usps = [
        {
            "num": "USP 01",
            "title": "Clause-Level Specification Matching",
            "tag": "EXACT REGULATORY CITATIONS",
            "desc": "Generic keyword search merely suggests standard numbers (e.g. 'IS 1786'). BharatStandards AI identifies the specific clauses, tables, and acceptance criteria (e.g., Table 3 for Fe 500D yield strength, Clause 9.2 for total elongation, Clause 8.2 for chemical composition).",
            "benefit": "Enables procurement officers to paste direct clause citations into tender documents without reading 50-page standard booklets."
        },
        {
            "num": "USP 02",
            "title": "Automated GFR 144(i) Anti-Bias Engine",
            "tag": "STATUTORY DE-BIASING & FAIR COMPETITION",
            "desc": "Built-in gazetteer scanner checks specifications for restrictive brand names (e.g., 'Tata Tiscon', 'Havells', 'Aashirvaad', 'Dell'). Automatically de-biases the text into neutral functional descriptions and appends the mandatory '(or equivalent conforming to IS...)' clause.",
            "benefit": "Eliminates single-vendor lock-in, shields officers from audit inquiries, and opens procurement to MSMEs."
        },
        {
            "num": "USP 03",
            "title": "Historical Supersession Auto-Correction",
            "tag": "PREVENTS RETIRED STANDARDS IN TENDERS",
            "desc": "Maintains an active registry of deprecated, revised, and superseded standards. When an engineer specifies 'IS 1139:1966', the engine flags the obsolete citation and auto-upgrades the tender to 'IS 1786:2008' with official BIS supersession notes.",
            "benefit": "Prevents tender legal challenges, court stays, and vendor disqualification disputes."
        },
        {
            "num": "USP 04",
            "title": "Statutory QCO Legal Verification",
            "tag": "MANDATORY ISI CERTIFICATION ENFORCEMENT",
            "desc": "Cross-references procurement items against Gazette Notifications issued by DPIIT, Ministry of Steel, MeitY, and Ministry of Power. Inserts the legally mandatory tender clause requiring suppliers to hold a valid BIS standard mark license.",
            "benefit": "Enforces national product quality laws and prevents substandard goods from entering government infrastructure."
        }
    ]

    for idx, u in enumerate(usps):
        row = idx // 2
        col = idx % 2
        x = Inches(0.8 + (col * 5.95))
        y = Inches(1.55 + (row * 2.75))
        
        card = create_card(s6, x, y, Inches(5.78), Inches(2.55), bg_color=CARD_BG, border_color=CARD_BORDER)
        tf = card.text_frame
        tf.margin_left = Inches(0.25)
        tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.2)

        p1 = tf.paragraphs[0]
        p1.text = f"{u['num']}  •  {u['tag']}"
        p1.font.name = FONT_HEADING
        p1.font.size = Pt(9.5)
        p1.font.bold = True
        p1.font.color.rgb = SAFFRON

        p2 = tf.add_paragraph()
        p2.text = u['title']
        p2.font.name = FONT_HEADING
        p2.font.size = Pt(13)
        p2.font.bold = True
        p2.font.color.rgb = NAVY_DARK
        p2.space_before = Pt(3)

        p3 = tf.add_paragraph()
        p3.text = u['desc']
        p3.font.name = FONT_BODY
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = SLATE_DARK
        p3.space_before = Pt(4)

        p4 = tf.add_paragraph()
        p4.text = f"Key Benefit: {u['benefit']}"
        p4.font.name = FONT_BODY
        p4.font.size = Pt(9)
        p4.font.bold = True
        p4.font.color.rgb = EMERALD
        p4.space_before = Pt(4)

    # =========================================================================
    # SLIDE 7: Feasibility, Viability & Regulatory Alignment
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, BG_LIGHT)
    add_header(s7, "Feasibility & Regulatory Alignment", "Practicality, Scalability, and Legal Defensibility")

    feasibility_pillars = [
        {
            "title": "TECHNICAL FEASIBILITY",
            "tag": "LIGHTWEIGHT & LOW LATENCY",
            "color": NAVY_DARK,
            "items": [
                ("Low Computational Footprint", "Sub-50ms inference time on standard multi-core CPU instances without needing multi-GPU infrastructure."),
                ("Zero Hallucinations", "Deterministic scoring algorithms guarantee explainable, auditable recommendations suitable for public finance scrutiny."),
                ("Microservice Ready", "Containerized Docker architecture allows instant integration as a pre-validation microservice on GeM / CPPP portals."),
                ("Scalability", "Easily scales to index all 25,000+ Indian Standards and 100,000+ annual tender specifications.")
            ]
        },
        {
            "title": "REGULATORY & LEGAL ALIGNMENT",
            "tag": "100% STATUTORY CONFORMANCE",
            "color": SAFFRON,
            "items": [
                ("General Financial Rules (GFR 2017)", "Enforces Rule 144(i) requiring functional parameters and prohibiting unjustified brand citations."),
                ("Bureau of Indian Standards Act 2016", "Ensures all public procurement references active, reaffirmed national standards with mandatory ISI marks."),
                ("Public Procurement (Make in India) Order", "Encourages domestic value addition by removing restrictive foreign-only qualification clauses."),
                ("Central Vigilance Commission (CVC)", "Eliminates tailor-made tender specifications that favor specific pre-selected vendors.")
            ]
        },
        {
            "title": "INTEGRATION & OPERATIONAL VIABILITY",
            "tag": "INSTANT ADOPTION PATHWAY",
            "color": EMERALD,
            "items": [
                ("GeM Pre-Publishing Check", "Can operate as an automated validation gatekeeper when procurement officers create bids on GeM."),
                ("Audit Trail & Compliance Score", "Generates an objective 0-100 Compliance Health Score that can be filed with technical tender approvals."),
                ("Public Standards Browser", "Enables officers to browse, search, and verify Indian Standards by Division Council, QCO, and commodity."),
                ("Zero Retraining Friction", "Simple web interface requires zero technical training for government administrative staff.")
            ]
        }
    ]

    for idx, fp in enumerate(feasibility_pillars):
        x = Inches(0.8 + (idx * 3.98))
        card = create_card(s7, x, Inches(1.5), Inches(3.8), Inches(5.4), bg_color=CARD_BG, border_color=CARD_BORDER)
        tf = card.text_frame
        tf.margin_left = Inches(0.25)
        tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.25)

        p_t = tf.paragraphs[0]
        p_t.text = fp['title']
        p_t.font.name = FONT_HEADING
        p_t.font.size = Pt(12)
        p_t.font.bold = True
        p_t.font.color.rgb = fp['color']

        p_tag = tf.add_paragraph()
        p_tag.text = fp['tag']
        p_tag.font.name = FONT_HEADING
        p_tag.font.size = Pt(8.5)
        p_tag.font.bold = True
        p_tag.font.color.rgb = SLATE_MUTED
        p_tag.space_before = Pt(2)

        p_div = tf.add_paragraph()
        p_div.text = "—" * 28
        p_div.font.size = Pt(8)
        p_div.font.color.rgb = CARD_BORDER
        p_div.space_before = Pt(3)

        for heading, body in fp['items']:
            p_h = tf.add_paragraph()
            p_h.text = f"• {heading}"
            p_h.font.name = FONT_HEADING
            p_h.font.size = Pt(10)
            p_h.font.bold = True
            p_h.font.color.rgb = NAVY_DARK
            p_h.space_before = Pt(6)

            p_b = tf.add_paragraph()
            p_b.text = f"  {body}"
            p_b.font.name = FONT_BODY
            p_b.font.size = Pt(9)
            p_b.font.color.rgb = SLATE_DARK
            p_b.space_before = Pt(1)

    # =========================================================================
    # SLIDE 8: Impact & Stakeholder Benefits
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8, BG_LIGHT)
    add_header(s8, "Impact & Stakeholder Benefits", "Transforming Public Procurement Transparency & Efficiency at National Scale")

    stakeholders = [
        {
            "role": "Government Procurement Officers",
            "entity": "CPWD • NHAI • FCI • Railways • Defense • State PSUs",
            "impact": "90% Reduction in Drafting Time",
            "impact_color": EMERALD,
            "points": [
                "Eliminates hours of manual search across technical standard manuals.",
                "Zero risk of audit objections or vigilance inquiries due to automated GFR 144(i) verification.",
                "Instant, exportable procurement schedules ready for direct publishing on GeM."
            ]
        },
        {
            "role": "Domestic Industry & MSMEs",
            "entity": "Indian Manufacturers & Startups",
            "impact": "Level Playing Field & Fair Access",
            "impact_color": SAFFRON,
            "points": [
                "Strips unfair brand names and restrictive single-vendor criteria from public tenders.",
                "Enables any certified domestic manufacturer meeting the Indian Standard to participate and win.",
                "Bolsters the 'Make in India' and 'Atmanirbhar Bharat' vision in public procurement."
            ]
        },
        {
            "role": "Bureau of Indian Standards (BIS)",
            "entity": "National Standards Body of India",
            "impact": "Enforced Standards Adoption",
            "impact_color": NAVY_DARK,
            "points": [
                "Accelerates the systematic adoption of Indian Standards across all 14 Division Councils.",
                "Ensures statutory Quality Control Orders (QCOs) are enforced at the point of procurement.",
                "Provides data-driven analytics on standard usage trends across government ministries."
            ]
        },
        {
            "role": "Taxpayers & Public Infrastructure",
            "entity": "Citizen Welfare & National Assets",
            "impact": "Higher Quality & Value for Money",
            "impact_color": EMERALD,
            "points": [
                "Prevents substandard, non-certified materials from entering bridges, highways, and public buildings.",
                "Ensures public nutrition standards (e.g. Fortified Rice Kernels, PDS Wheat) meet rigorous micronutrient criteria.",
                "Maximizes the value of taxpayer funds through transparent, competitive bidding."
            ]
        }
    ]

    for idx, sh in enumerate(stakeholders):
        row = idx // 2
        col = idx % 2
        x = Inches(0.8 + (col * 5.95))
        y = Inches(1.55 + (row * 2.75))
        
        card = create_card(s8, x, y, Inches(5.78), Inches(2.55), bg_color=CARD_BG, border_color=CARD_BORDER)
        tf = card.text_frame
        tf.margin_left = Inches(0.25)
        tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.2)

        # Entity
        p_ent = tf.paragraphs[0]
        p_ent.text = sh['entity'].upper()
        p_ent.font.name = FONT_HEADING
        p_ent.font.size = Pt(8.5)
        p_ent.font.bold = True
        p_ent.font.color.rgb = SAFFRON

        # Role
        p_role = tf.add_paragraph()
        p_role.text = sh['role']
        p_role.font.name = FONT_HEADING
        p_role.font.size = Pt(13)
        p_role.font.bold = True
        p_role.font.color.rgb = NAVY_DARK
        p_role.space_before = Pt(2)

        # Impact Badge
        p_imp = tf.add_paragraph()
        p_imp.text = f"★ IMPACT: {sh['impact']}"
        p_imp.font.name = FONT_HEADING
        p_imp.font.size = Pt(9.5)
        p_imp.font.bold = True
        p_imp.font.color.rgb = sh['impact_color']
        p_imp.space_before = Pt(2)

        for pt in sh['points']:
            p_pt = tf.add_paragraph()
            p_pt.text = f"• {pt}"
            p_pt.font.name = FONT_BODY
            p_pt.font.size = Pt(9.5)
            p_pt.font.color.rgb = SLATE_DARK
            p_pt.space_before = Pt(4)

    # =========================================================================
    # SLIDE 9: Hackathon Implementation Roadmap & Milestones
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9, BG_LIGHT)
    add_header(s9, "Hackathon Execution Roadmap", "Strategic Milestone Plan from Round 1 to Grand Finale Deployment")

    phases = [
        {
            "phase": "PHASE 1 (CURRENT)",
            "title": "Idea Formulation & Pipeline Architecture",
            "tag": "ROUND 1 DELIVERABLE",
            "color": SAFFRON,
            "tasks": [
                "Exhaustive research on BIS Act 2016, GFR 144(i), and QCO statutory mandates.",
                "Formalized hybrid retrieval algorithm (BM25 + TF-IDF Cosine + Parameter Boosting).",
                "Built initial taxonomy across all 14 BIS Division Councils and brands gazetteer.",
                "Defined end-to-end multi-format parsing pipeline (PDF, DOCX, TXT)."
            ]
        },
        {
            "phase": "PHASE 2 (POST-SELECTION)",
            "title": "Core Retrieval Engine & Corpus Expansion",
            "tag": "PROTOTYPE DEVELOPMENT",
            "color": NAVY_DARK,
            "tasks": [
                "Expand standards catalog to 250+ high-frequency procurement standards.",
                "Develop domain-specific regex and NLP parameter extractors for top 5 procurement sectors.",
                "Implement clause-level citation mapping for physical, mechanical, and electrical tests.",
                "Build automated evaluation benchmark on 50+ real-world government tenders."
            ]
        },
        {
            "phase": "PHASE 3 (MENTORSHIP)",
            "title": "GeM Integration & Advanced Auditing",
            "tag": "FEATURE ENHANCEMENT",
            "color": NAVY_DARK,
            "tasks": [
                "Implement side-by-side text sanitization diff with instant red/green visualizer.",
                "Build GeM bid schedule generator (Markdown, HTML, JSON export).",
                "Integrate Bhashini API for multi-lingual regional tender specification support.",
                "Incorporate feedback from BIS and GeM domain mentors."
            ]
        },
        {
            "phase": "PHASE 4 (FINALE)",
            "title": "Grand Finale Deployment & Pilot Testing",
            "tag": "PRODUCTION DEPLOYMENT",
            "color": EMERALD,
            "tasks": [
                "Dockerized microservice deployment ready for MeghRaj / NIC Cloud.",
                "Live demonstration on real-world tenders from FCI (Foodgrains) and CPWD (Civil).",
                "Security and performance load testing ensuring sub-50ms query latency.",
                "Final presentation and live system demonstration to Hackathon Grand Jury."
            ]
        }
    ]

    for idx, ph in enumerate(phases):
        x = Inches(0.8 + (idx * 2.98))
        card = create_card(s9, x, Inches(1.5), Inches(2.82), Inches(5.4), bg_color=CARD_BG, border_color=CARD_BORDER)
        tf = card.text_frame
        tf.margin_left = Inches(0.2)
        tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.2)

        p_ph = tf.paragraphs[0]
        p_ph.text = ph['phase']
        p_ph.font.name = FONT_HEADING
        p_ph.font.size = Pt(8.5)
        p_ph.font.bold = True
        p_ph.font.color.rgb = ph['color']

        p_t = tf.add_paragraph()
        p_t.text = ph['title']
        p_t.font.name = FONT_HEADING
        p_t.font.size = Pt(11)
        p_t.font.bold = True
        p_t.font.color.rgb = NAVY_DARK
        p_t.space_before = Pt(3)

        p_tag = tf.add_paragraph()
        p_tag.text = ph['tag']
        p_tag.font.name = FONT_HEADING
        p_tag.font.size = Pt(8)
        p_tag.font.bold = True
        p_tag.font.color.rgb = SLATE_MUTED
        p_tag.space_before = Pt(2)

        p_div = tf.add_paragraph()
        p_div.text = "—" * 22
        p_div.font.size = Pt(8)
        p_div.font.color.rgb = CARD_BORDER
        p_div.space_before = Pt(2)

        for t in ph['tasks']:
            p_tsk = tf.add_paragraph()
            p_tsk.text = f"• {t}"
            p_tsk.font.name = FONT_BODY
            p_tsk.font.size = Pt(9.5)
            p_tsk.font.color.rgb = SLATE_DARK
            p_tsk.space_before = Pt(6)

    # =========================================================================
    # SLIDE 10: Conclusion & Summary (Dark Navy Closing)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10, NAVY_DARK)

    # Decorative saffron top strip
    strip10 = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12))
    strip10.fill.solid()
    strip10.fill.fore_color.rgb = SAFFRON
    strip10.line.fill.background()

    # Title
    t_box10 = s10.shapes.add_textbox(Inches(1.0), Inches(0.8), Inches(11.33), Inches(1.0))
    tf10 = t_box10.text_frame
    p10_1 = tf10.paragraphs[0]
    p10_1.text = "CONCLUSION & SUMMARY"
    p10_1.font.name = FONT_HEADING
    p10_1.font.size = Pt(12)
    p10_1.font.bold = True
    p10_1.font.color.rgb = SAFFRON

    p10_2 = tf10.add_paragraph()
    p10_2.text = "Why BharatStandards AI is the Right Solution for SIH26108"
    p10_2.font.name = FONT_HEADING
    p10_2.font.size = Pt(24)
    p10_2.font.bold = True
    p10_2.font.color.rgb = WHITE
    p10_2.space_before = Pt(3)

    # 3 Summary Cards
    summary_cards = [
        {
            "title": "Solves a Critical National Need",
            "desc": "Brings rigorous standardization, transparency, and anti-bias auditing to India's ₹15 Lakh Crore public procurement ecosystem across GeM and CPPP portals."
        },
        {
            "title": "Explainable & Legally Sound",
            "desc": "Built on deterministic, verifiable hybrid retrieval with clause-level citations and direct links to Central Government Gazette QCO notifications—zero hallucination risk."
        },
        {
            "title": "Ready for Rapid Deployment",
            "desc": "Lightweight, highly scalable architecture deployable on government cloud infrastructure (NIC / MeghRaj) with standard REST APIs for seamless GeM integration."
        }
    ]

    for idx, sc in enumerate(summary_cards):
        x = Inches(1.0 + (idx * 3.85))
        card = create_card(s10, x, Inches(2.2), Inches(3.6), Inches(2.4), bg_color=NAVY_LIGHT, border_color=SAFFRON)
        tf = card.text_frame
        tf.margin_left = Inches(0.25)
        tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.25)

        p = tf.paragraphs[0]
        p.text = sc['title']
        p.font.name = FONT_HEADING
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = WHITE

        p_d = tf.add_paragraph()
        p_d.text = sc['desc']
        p_d.font.name = FONT_BODY
        p_d.font.size = Pt(10.5)
        p_d.font.color.rgb = RGBColor(215, 225, 245)
        p_d.space_before = Pt(8)

    # Thank you & Q&A Box
    qa_card = create_card(s10, Inches(1.0), Inches(5.0), Inches(11.33), Inches(1.6), bg_color=NAVY_LIGHT, border_color=CARD_BORDER)
    tf_qa = qa_card.text_frame
    tf_qa.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_qa.margin_left = Inches(0.4)

    p_qa1 = tf_qa.paragraphs[0]
    p_qa1.text = "THANK YOU! WE ARE READY FOR YOUR QUESTIONS."
    p_qa1.font.name = FONT_HEADING
    p_qa1.font.size = Pt(16)
    p_qa1.font.bold = True
    p_qa1.font.color.rgb = SAFFRON

    p_qa2 = tf_qa.add_paragraph()
    p_qa2.text = "Team Innovators  •  Smart India Hackathon 2026  •  Problem Statement SIH26108"
    p_qa2.font.name = FONT_BODY
    p_qa2.font.size = Pt(11)
    p_qa2.font.color.rgb = WHITE
    p_qa2.space_before = Pt(3)

    p_qa3 = tf_qa.add_paragraph()
    p_qa3.text = "Ministry of Consumer Affairs, Food & Public Distribution | Bureau of Indian Standards (BIS)"
    p_qa3.font.name = FONT_BODY
    p_qa3.font.size = Pt(10)
    p_qa3.font.color.rgb = RGBColor(180, 195, 220)
    p_qa3.space_before = Pt(2)

    prs.save(OUTPUT_FILE)
    print(f"Successfully generated SIH 2026 Presentation at: {OUTPUT_FILE}")

if __name__ == "__main__":
    build_presentation()
