# Sample Procurement Tenders Catalog (SIH-108 Testing Suite)

This directory contains **14 diverse, realistic Indian public procurement tender specifications** covering multiple sectors, departments, and file formats (`.txt`, `.pdf`, `.docx`).

You can test the engine by:
1. **Drag-and-Drop or File Upload:** Drag any `.pdf`, `.docx`, or `.txt` file into the upload zone on the web dashboard at `http://127.0.0.1:8000`.
2. **Copy & Paste:** Open any `.txt` file, copy the content, and paste it into the tender specification textarea.
3. **CLI / API:** Send the file via `curl` or Python requests to `/api/v1/analyze-file`.

## Test Cases Overview

| # | File Name | Formats | Sector / Ministry | Key Features & Test Objective | Expected BIS Standard | Compliance Alerts |
|---|-----------|---------|-------------------|--------------------------------|-----------------------|-------------------|
| 1 | `01_food_fortified_rice_frk` | `.txt`, `.pdf` | Food & Public Distribution (DFPD/FCI) | Fortified Rice Kernels, Iron, Folic Acid, B12 micronutrients | **IS 17782** | Clean / No Bias |
| 2 | `02_food_pds_wheat_atta_biased` | `.txt`, `.docx` | Food & Civil Supplies | Brand Bias (`Aashirvaad`, `Fortune`), Chakki atta parameters | **IS 1155** | GFR 144(i) Bias Detected & Auto-Sanitized |
| 3 | `03_food_jute_bags_50kg_fci` | `.txt`, `.pdf` | Foodgrain Packaging (FCI) | 50kg Twill Jute Bags, dimensions, tensile breaking strength | **IS 12650** | Clean / No Bias |
| 4 | `04_food_packaged_drinking_water_biased` | `.txt` | IRCTC / Food Safety | Brand Bias (`Bisleri`, `Aquafina`, `Kinley`), TDS, RO | **IS 14543** | Brand Bias + Mandatory QCO Alert |
| 5 | `05_civil_flyover_tmt_rebars_obsolete_biased` | `.txt`, `.pdf` | Civil Infrastructure (CPWD) | Obsolete `IS 1139` + Brand Bias (`Tata Tiscon`, `Jindal Panther`) | **IS 1786** | Obsolete Standard Replaced + Steel QCO |
| 6 | `06_civil_ppc_cement_biased` | `.txt`, `.docx` | Highway Engineering (NHAI) | Brand Bias (`UltraTech`, `ACC`, `Ambuja`), Flyash PPC | **IS 1489 Part 1** | Brand Bias + Cement Mandatory QCO |
| 7 | `07_civil_hdpe_water_pipes_jjm` | `.txt`, `.pdf` | Water Infrastructure (Jal Jeevan) | PE 100, PN 10, 110mm outer diameter HDPE pipes | **IS 4984** | Mandatory Polyethylene QCO Alert |
| 8 | `08_electrical_pvc_armoured_cables_biased` | `.txt`, `.docx` | Metro Rail Electrical (DMRC) | Brand Bias (`Havells`, `Polycab`, `Finolex`), 1.1kV 4-core | **IS 1554 Part 1** | Brand Bias + Electrical Cable QCO |
| 9 | `09_electrical_solar_grid_inverter` | `.txt` | Renewable Energy (MNRE/SECI) | 50 kW 3-phase grid-tied string inverter, THD < 3%, MPPT | **IS 16221 Part 2** | Mandatory MeitY/MNRE CRO Order |
| 10 | `10_safety_industrial_helmets_qco` | `.txt`, `.pdf` | Personal Protective Equipment (BRO) | Brand Bias (`3M`, `Karam`), 5.0 kN shock absorption | **IS 2925** | Brand Bias + Mandatory PPE QCO |
| 11 | `11_safety_n95_respiratory_masks` | `.txt` | Healthcare PPE (AIIMS) | N95 / FFP2 particulate respirator, 95% PFE, breathing resistance | **IS 9473** | Respiratory PPE Standard |
| 12 | `12_it_laptops_brand_biased_dell` | `.txt`, `.docx` | IT & e-Governance | Restrictive Single-Vendor Bias (`Dell Latitude`, `HP EliteBook`) | **IS 13252 Part 1** | GFR 144(i) Brand Struck Out + MeitY CRO |
| 13 | `13_mechanical_centrifugal_pump` | `.txt` | Municipal Waterworks | 150 m3/hr, 45m head, 30 kW motor end-suction pump | **IS 1520** | Mechanical Pump Performance Standard |
| 14 | `14_textiles_cotton_hospital_bedsheets` | `.txt` | Medical Linen (DGHS) | 100% cotton, 230x150 cm, 180 TC, 140 GSM bedsheets | **IS 745** | Textile Strength & Fastness Standard |
