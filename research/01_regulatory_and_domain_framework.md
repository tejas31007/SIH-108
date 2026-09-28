# 01. Regulatory & Domain Framework

## 1. Executive Context: Public Procurement in India

Public procurement accounts for approximately **20% to 25% of India's GDP**. It is conducted across multiple tiers:
* **Central Ministries & Departments**
* **Public Sector Undertakings (PSUs) & Enterprises**
* **State Governments & Municipal Bodies**
* **Defense & Railway Procurement**

Procurement happens predominantly through digital portals such as:
1. **GeM (Government e-Marketplace):** The primary e-commerce portal for common use goods and services.
2. **CPPP (Central Public Procurement Portal):** For high-value works, customized tenders, and global tenders.

To ensure quality, safety, and competitiveness, public procurement in India is bound by strict statutory and financial rules.

---

## 2. Bureau of Indian Standards (BIS) & The BIS Act, 2016

### 2.1 The National Standards Body
The **Bureau of Indian Standards (BIS)** is established under the **Bureau of Indian Standards Act, 2016**, operating under the aegis of the **Ministry of Consumer Affairs, Food & Public Distribution**.

BIS is responsible for:
1. **Standard Formulation:** Developing Indian Standards (denoted as `IS <number>:<year>`).
2. **Conformity Assessment:** Operating certification schemes:
   * **Scheme-I (ISI Mark Scheme):** Product certification based on factory audits and laboratory testing.
   * **Scheme-II (Compulsory Registration Scheme - CRS):** Self-declaration of conformity for electronics and IT goods under MeitY/BIS.
   * **Scheme-IV (Grant of Certificate of Conformity):** Lot-based inspections.
3. **Hallmarking:** Compulsory hallmarking of precious metals (Gold and Silver).
4. **Laboratory Accreditation:** Maintaining national reference laboratories.

### 2.2 Nomenclature of Indian Standards
An Indian Standard follows a strict hierarchical naming convention:
$$\text{IS } \underbrace{1786}_{\text{Standard No.}} : \underbrace{2008}_{\text{Year of Formulation}} \; (\text{Reaffirmed } 2018)$$
* **Standard Number:** Unique identifier for the subject.
* **Parts & Sections:** Complex subjects are partitioned (e.g., `IS 1239 (Part 1): 2004` - Mild steel tubes).
* **Year of Publication:** The year the specific revision was published.
* **Reaffirmation:** BIS mandates that standards undergo periodic review (typically every 5 years) to ensure technological relevance. If no change is needed, it is "Reaffirmed".
* **Amendments:** Numbered slips (`Amendment No. 1, 2...`) published to alter specific clauses without reissuing the whole standard.

---

## 3. General Financial Rules (GFR 2017): Rule 144(i)

The **General Financial Rules (GFR)** issued by the Ministry of Finance constitute the statutory guidelines for all public procurement.

### 3.1 Text of Rule 144(i)
> *"The description of the subject matter of procurement to the extent practicable should:*
> 1. *Be **objective, functional, generic and measurable**.*
> 2. *Set out the relevant characteristics of the goods, works or service to be procured.*
> 3. ***Not indicate a requirement for or reference to a particular trademark or trade name, patent, design or type, specific origin or producer**, unless there is no sufficiently precise or intelligible way of describing the characteristics of the goods, works or service to be procured and provided that words such as **'or equivalent'** are included in the specifications.*
> 4. *The technical specifications should, to the extent practicable, **be based on national standards, where such standards exist**, or on relevant international standards or on technical regulations."*

### 3.2 Key Violations Observed in Current Tenders
1. **Brand Bias / Trademark Insertion:**
   * *Violation:* "Tender for purchase of Core i7 Dell OptiPlex or HP EliteDesk Desktop PCs."
   * *Correct Form:* "Desktop PC conforming to IS 16046 / relevant BIS standards with specified benchmark score, RAM, and processor cores."
2. **Gold-Plating / Over-Specification:**
   * Crafting specifications with tolerances or proprietary features that only a single vendor’s catalog product satisfies (e.g., specifying an exact chassis dimension `412mm x 185mm x 350mm` when standard dimensions vary).
3. **Omitting 'Or Equivalent':**
   * Mentioning a brand without the legally mandatory suffix "or equivalent".
4. **Ignoring National Standards:**
   * Specifying foreign standards (e.g., ASTM, DIN, BS) when an equivalent or harmonized Indian Standard (IS) exists.

---

## 4. Quality Control Orders (QCOs)

### 4.1 What is a QCO?
Under **Section 16 of the BIS Act, 2016**, the Central Government (via line ministries such as DPIIT, Ministry of Steel, Ministry of Heavy Industries, Ministry of Electronics and IT) issues **Quality Control Orders (QCOs)** in the public interest.

### 4.2 Legal Implications of QCOs
* **Mandatory Certification:** Once a product is brought under a QCO, it **cannot be manufactured, imported, stored, sold, or distributed in India without conforming to the specified Indian Standard and bearing the BIS Standard Mark (ISI mark or CRS registration)**.
* **Criminal Liability:** Non-compliance invites penal action, including product seizures, fines, and imprisonment under Section 29 of the BIS Act, 2016.
* **Procurement Impact:** A government entity **cannot legally procure** non-BIS certified goods if that item category is governed by a notified QCO.

### 4.3 High-Profile Sectors Under Mandatory QCOs
1. **Steel & Iron Products:** Steel bars, wire rods, pipes (Ministry of Steel).
2. **Electrical Products:** Cables, switches, circuit breakers, domestic appliances.
3. **Chemicals & Petrochemicals:** Caustic soda, acetic acid, PVC pipes.
4. **Toys & Safety Equipment:** Safety helmets (IS 2925), safety shoes, children's toys.
5. **Civil Construction Materials:** Portland Pozzolana Cement (IS 1489), Ordinary Portland Cement (IS 269), structural steel (IS 2062).

---

## 5. Government e-Marketplace (GeM) Specifications Schema

GeM organizes products into a structured hierarchy:
1. **Category:** High-level product group (e.g., "Air Conditioner", "Reinforcement Steel").
2. **Golden Parameters:** Core technical parameters that determine basic product classification and filtering (e.g., Tonnage, Energy Star Rating, Refrigerant Type).
3. **Catalog Specifications:** Product attributes submitted by OEM sellers verified against BIS/test lab reports.
4. **Buyer Added Bid Specific Additional Terms and Conditions (ATC):** Custom clauses added by procurement officers—this is the **primary source of errors, bias, and obsolete standard references**.

### Summary of System Value Proposition
Our recommendation engine will:
* Automatically validate Buyer ATC and specification schedules against **GFR 144(i)**.
* Intercept non-compliant tenders before publication.
* Enforce **mandatory QCO verification** at the point of tender generation.
* Suggest standard, generic, BIS-aligned technical clauses.
