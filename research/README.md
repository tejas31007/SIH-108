# SIH26108: AI-Powered Recommendation Engine for Indian Standards (BIS)

## Research & Engineering Dossier

Welcome to the foundational research repository for **Smart India Hackathon Problem Statement SIH26108**:
> **Title:** AI-Powered Recommendation Engine for Identifying Applicable Indian Standards for Procurement Specifications  
> **Ministry:** Ministry of Consumer Affairs, Food & Public Distribution (Bureau of Indian Standards - BIS)  
> **Theme:** Smart Automation (Software)

---

### Table of Contents

| Document | Focus Area | Description |
| :--- | :--- | :--- |
| [**01_regulatory_and_domain_framework.md**](./01_regulatory_and_domain_framework.md) | Legal & Procurement Mandates | Deep-dive into BIS Act 2016, GFR 2017 Rule 144(i), Quality Control Orders (QCOs), and GeM procurement guidelines. |
| [**02_bis_standards_dataset_architecture.md**](./02_bis_standards_dataset_architecture.md) | Data Taxonomy & Knowledge Base | Structural analysis of Indian Standards (IS), life-cycle states (Active, Superseded, Withdrawn), and database schema design. |
| [**03_nlp_parameter_extraction_pipeline.md**](./03_nlp_parameter_extraction_pipeline.md) | Document Parsing & Entity Extraction | NLP methodologies for extracting technical parameters, dimensions, materials, and test methods from tender specifications. |
| [**04_hybrid_retrieval_and_recommendation_engine.md**](./04_hybrid_retrieval_and_recommendation_engine.md) | Search & Recommendation AI | Multi-stage Hybrid Retrieval (BM25 + Dense Embeddings + Cross-Encoder Reranker) and clause-level citation matching. |
| [**05_anti_bias_and_compliance_audit_engine.md**](./05_anti_bias_and_compliance_audit_engine.md) | Anti-Bias & GFR 144(i) Verification | Algorithms and heuristics for detecting proprietary vendor bias, brand name leakage, and QCO mandatory compliance checks. |
| [**06_frontend_strategy_and_stitch_ai_guide.md**](./06_frontend_strategy_and_stitch_ai_guide.md) | UI/UX & Stitch AI Implementation | Blueprint for using Stitch AI to design frontend components, export code, and integrate with our Python/FastAPI backend. |

---

### Executive Summary

#### The Problem
Public procurement in India spans over ₹20+ Lakh Crore annually across central/state ministries, PSUs, and defense organizations. Under Indian procurement law:
1. **Standards Conformity:** Procurement must comply with Indian Standards (IS) published by BIS.
2. **Quality Control Orders (QCOs):** Dozens of product categories (steel, cables, toys, electronics, cement) legally mandate ISI certification before purchase.
3. **GFR Rule 144(i) Non-Discrimination:** Specifications must be objective, functional, and generic—expressly prohibiting brand names or restrictive criteria that artificially limit competition.

In practice, procurement officers manually draft specifications. They frequently:
* Cite **obsolete/superseded** standards.
* Inadvertently copy **proprietary specifications** from a favorite manufacturer's catalog (violating GFR 144(i)).
* Miss mandatory **Quality Control Orders**, procuring non-certified products.

#### The Solution
An intelligent, explainable decision-support system:
* Ingests tender PDFs and raw specification text.
* Extracts core technical parameters via domain-adapted NLP.
* Recommends the exact applicable Indian Standards (IS codes, titles, editions, and specific clauses) using hybrid dense-sparse retrieval.
* Automatically audits the text for single-vendor bias and mandatory QCO compliance.
* Generates an audit-ready, GeM-compliant procurement specification sheet.
