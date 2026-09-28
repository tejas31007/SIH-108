"""
Script to generate realistic procurement tender sample files across multiple formats (.txt, .pdf, .docx)
in the sample_files/ directory for comprehensive testing of SIH-108.
"""
import os
import pymupdf as fitz
import docx
from docx.shared import Pt, Inches, RGBColor

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SAMPLE_DIR = os.path.join(BASE_DIR, "sample_files")
os.makedirs(SAMPLE_DIR, exist_ok=True)

SAMPLES = [
    {
        "id": "01_food_fortified_rice_frk",
        "title": "Procurement of Fortified Rice Kernels (FRK) for PM POSHAN and PDS Scheme",
        "tender_no": "FCI/NZ/PDS/FRK/2026/04",
        "dept": "Department of Food & Public Distribution (DFPD) / Food Corporation of India",
        "text": """NOTICE INVITING TENDER (NIT)
Tender No: FCI/NZ/PDS/FRK/2026/04
Department: Department of Food & Public Distribution, Ministry of Consumer Affairs, Food & PD

SCHEDULE OF REQUIREMENTS & TECHNICAL SPECIFICATIONS:

1. ITEM DESCRIPTION:
Supply of Fortified Rice Kernels (FRK) manufactured by extrusion technology for blending with custom milled rice (CMR) under the Centrally Sponsored Scheme of Rice Fortification for Targeted Public Distribution System (TPDS) and PM POSHAN.

2. TECHNICAL PARAMETERS & COMPOSITION:
- Physical Appearance: FRK shall closely resemble normal milled rice in length, breadth, translucency, and cooking characteristics.
- Length-to-Width Ratio: Medium slender grain profile matching raw milled rice.
- Moisture Content: Maximum 12.0% by weight.
- Micronutrient Premix Composition (per kg of FRK):
  * Iron (as Ferric Pyrophosphate or Sodium Iron EDTA): 28.0 mg to 42.5 mg per 100g
  * Folic Acid: 75 mcg to 125 mcg per 100g
  * Vitamin B12 (Cyanocobalamin): 0.75 mcg to 1.25 mcg per 100g
- Shelf Life: Minimum 12 months under standard storage conditions.
- Disintegration Time: Not less than 15 minutes in boiling water without forming paste.

3. STATUTORY COMPLIANCE & QUALITY CERTIFICATION:
The supplier must possess a valid Bureau of Indian Standards (BIS) license / FSSAI manufacturing license and provide batch testing certificate from an NABL accredited laboratory for each consignment.
""",
        "formats": ["txt", "pdf"]
    },
    {
        "id": "02_food_pds_wheat_atta_biased",
        "title": "Supply of Packaged Whole Wheat Atta for NFSA Fair Price Shops",
        "tender_no": "FCS/CIVIL/WHEAT-ATTA/2026/18",
        "dept": "State Department of Food, Civil Supplies & Consumer Affairs",
        "text": """NOTICE INVITING TENDER (NIT)
Tender No: FCS/CIVIL/WHEAT-ATTA/2026/18
Department: Directorate of Civil Supplies and Consumer Affairs

TECHNICAL SPECIFICATIONS & SPECIAL CONDITIONS:

1. SCOPE OF SUPPLY:
Supply of Chakki Whole Wheat Flour (Atta) in airtight 10 kg laminated polypacks for distribution across 1,200 Fair Price Shops under the National Food Security Act (NFSA).

2. TECHNICAL SPECIFICATIONS & MANDATORY BRAND REQUIREMENT:
- The supplied whole wheat atta must strictly match the premium texture, fineness, and organoleptic quality of Aashirvaad Shudh Chakki Atta or Fortune Chakki Fresh Atta. Only flour milled using traditional stone chakki process will be accepted.
- Moisture Content: Shall not exceed 13.0% by weight.
- Total Ash: Not more than 2.0% on dry weight basis.
- Acid Insoluble Ash: Maximum 0.10% by weight.
- Gluten (dry basis): Minimum 6.0%.
- Crude Fibre: Not less than 1.8% on dry basis.
- Free from insect infestation, rodent contamination, synthetic coloring, and chemical bleaches.

3. PACKAGING AND LABELLING:
Each 10 kg bag must be food-grade HDPE woven sack with inner LDPE liner. Delivery within 15 days of purchase order.
""",
        "formats": ["txt", "docx"]
    },
    {
        "id": "03_food_jute_bags_50kg_fci",
        "title": "Supply of 50 kg Capacity Twill Jute Bags for Storage and Transit of Foodgrains",
        "tender_no": "FCI/HARS/PROC/JUTE-BAGS/2026/91",
        "dept": "Food Corporation of India - Headquarters Procurement Wing",
        "text": """NOTICE INVITING TENDER (NIT)
Tender No: FCI/HARS/PROC/JUTE-BAGS/2026/91
Authority: Food Corporation of India, Procurement & Storage Division

TECHNICAL SPECIFICATIONS:

1. ITEM SPECIFICATION:
Supply of 50 kg capacity twill jute bags intended for packaging and long-term buffer stocking of Wheat and Paddy in Central Pool silos and godowns.

2. CONSTRUCTIONAL AND MECHANICAL PARAMETERS:
- Bag Type: Twill weave jute bag without seam defects.
- Nominal Capacity: 50 kg foodgrains.
- Outside Dimensions: Length 94 cm (+/- 1.5 cm) x Width 57 cm (+/- 1.0 cm).
- Tare Weight of Bag: 665 grams (+/- 10% on batch average).
- Warp Threads (Ends/dm): 76 +/- 4 ends per decimeter.
- Weft Threads (Picks/dm): 34 +/- 2 picks per decimeter.
- Breaking Strength:
  * Warp Direction: Minimum 350 N.
  * Weft Direction: Minimum 400 N.
- Seam Strength: Minimum 230 N along the stitched edges.
- Oil Content: Maximum 3.0% based on dry weight.
""",
        "formats": ["txt", "pdf"]
    },
    {
        "id": "04_food_packaged_drinking_water_biased",
        "title": "Supply of 1-Litre Sealed Packaged Drinking Water Bottles for Rail Canteens",
        "dept": "Indian Railway Catering & Tourism Corporation (IRCTC)",
        "tender_no": "IRCTC/CATG/WATER-BOTTLE/2026/09",
        "text": """TENDER DOCUMENT FOR SUPPLY OF PACKAGED DRINKING WATER
Tender No: IRCTC/CATG/WATER-BOTTLE/2026/09
Department: Catering & Tourism Services Corporation

SCHEDULE OF REQUIREMENTS:

1. PRODUCT DESCRIPTION:
Packaged drinking water in 1000 ml food-grade PET bottles with tamper-evident seal caps for catering on premium express trains and parliamentary canteens.

2. QUALITY & BRAND CRITERIA:
- The supplied packaged water must be of recognized national standard brands such as Bisleri or Aquafina or Kinley.
- Water treatment must involve multi-barrier purification: ozonation, sand filtration, activated carbon absorption, reverse osmosis (RO), and final ultra-violet (UV) sterilization.
- Total Dissolved Solids (TDS): Between 75 mg/l and 150 mg/l.
- Total Hardness (as CaCO3): Not exceeding 75 mg/l.
- pH Value: 6.5 to 8.5.
- Microbiological Criteria: Zero E. coli, coliform bacteria, and Pseudomonas aeruginosa per 250 ml sample.
- Compulsory BIS standard conformity and statutory license required under the Prevention of Food Adulteration / FSSAI rules.
""",
        "formats": ["txt"]
    },
    {
        "id": "05_civil_flyover_tmt_rebars_obsolete_biased",
        "title": "Supply of High Yield Strength Deformed TMT Steel Rebars for Flyover Pier Caps",
        "dept": "Central Public Works Department (CPWD) - Flyover Projects",
        "tender_no": "CPWD/DELHI/FLY-03/2026/01",
        "text": """GOVERNMENT OF INDIA - CENTRAL PUBLIC WORKS DEPARTMENT
NIT No: CPWD/DELHI/FLY-03/2026/01
Project: Construction of 6-Lane Elevated Corridor and Flyover Interchange

SECTION IV - TECHNICAL SPECIFICATIONS FOR REINFORCEMENT STEEL:

1. MATERIAL SPECIFICATIONS:
Supply of High Strength Deformed Steel Bars for concrete reinforcement in pier caps, deck slabs, and retaining walls.
The steel rebars must strictly conform to IS 1139:1966 for cold twisted steel bars.

2. APPROVED BRANDS & RESTRICTIONS:
Materials shall be procured exclusively from primary producers only: Tata Tiscon or Jindal Panther or SAIL. Rebars from secondary re-rollers or unapproved brands will be summarily rejected.

3. MECHANICAL AND CHEMICAL PARAMETERS:
- Grade: Fe 500D (Ductile grade for seismic zone IV construction).
- Nominal Diameters: 12 mm, 16 mm, 20 mm, 25 mm, and 32 mm.
- Yield Strength (0.2% proof stress): Minimum 500.0 N/mm2.
- Tensile Strength: Minimum 565.0 N/mm2 (Tensile to Yield ratio >= 1.10).
- Percentage Elongation at Fracture: Minimum 16.0%.
- Total Elongation at Maximum Force: Minimum 5.0%.
- Carbon: Maximum 0.25%, Sulphur: Maximum 0.040%, Phosphorus: Maximum 0.040%, (S+P) max 0.075%.
- Each bundle must bear manufacturer BIS Standard Mark certification under the Mandatory Steel Quality Control Order.
""",
        "formats": ["txt", "pdf"]
    },
    {
        "id": "06_civil_ppc_cement_biased",
        "title": "Procurement of Portland Pozzolana Cement (PPC) for Bridge Construction",
        "dept": "National Highways Authority of India (NHAI)",
        "tender_no": "NHAI/TECH/CEMENT-PPC/2026/77",
        "text": """NATIONAL HIGHWAYS AUTHORITY OF INDIA
Tender Notice No: NHAI/TECH/CEMENT-PPC/2026/77
Project: 4-Laning of National Highway Bypass Package 2

TECHNICAL SPECIFICATION SCHEDULE - CEMENT:

1. DESCRIPTION OF ITEM:
Supply of Flyash-based Portland Pozzolana Cement (PPC) in 50 kg HDPE bags for reinforced cement concrete (RCC) works, retaining structures, and pavement culverts.

2. SPECIFIC BRAND DIRECTIVE:
Tenderers must deliver cement produced by UltraTech Cement or ACC Cement or Ambuja Cement. Bids offering local or non-reputed cement brands shall not be considered.

3. PHYSICAL AND CHEMICAL REQUIREMENTS:
- Pozzolana Content: Pulverized fuel ash (fly ash) proportion between 15% and 35% by mass.
- Fineness (Specific Surface): Not less than 300 m2/kg by Blaine air permeability method.
- Setting Time: Initial setting time not less than 30 minutes; Final setting time not more than 600 minutes.
- Compressive Strength:
  * 72 +/- 1 hour (3 days): Minimum 16.0 MPa
  * 168 +/- 2 hours (7 days): Minimum 22.0 MPa
  * 672 +/- 4 hours (28 days): Minimum 33.0 MPa
- Soundness: Le Chatelier expansion not more than 10 mm; Autoclave expansion not more than 0.8%.
- Insoluble Residue: Not more than X + 4.0% by mass.
""",
        "formats": ["txt", "docx"]
    },
    {
        "id": "07_civil_hdpe_water_pipes_jjm",
        "title": "Procurement of HDPE Pipes for Rural Piped Drinking Water Supply",
        "dept": "Jal Jeevan Mission - Public Health Engineering Department (PHED)",
        "tender_no": "JJM/PHED/PIPE-HDPE/2026/142",
        "text": """JAL JEEVAN MISSION - PUBLIC HEALTH ENGINEERING DEPARTMENT
Tender No: JJM/PHED/PIPE-HDPE/2026/142
Sub-Mission: Har Ghar Jal Rural Water Supply Network

SCHEDULE OF REQUIREMENTS:

1. SCOPE OF SUPPLY:
Supply and delivery of High Density Polyethylene (HDPE) solid wall pipes for pressurized conveyance of potable drinking water from headworks to village distribution networks.

2. TECHNICAL CHARACTERISTICS:
- Raw Material: 100% virgin pre-compounded PE 100 polyethylene granules with carbon black content 2.0% to 2.5% uniformly dispersed.
- Nominal Outside Diameter (DN): 110 mm.
- Standard Dimension Ratio: SDR 17.
- Pressure Rating: PN 10 (1.0 MPa working pressure at 27 deg C).
- Minimum Required Strength (MRS): 10.0 MPa.
- Hydrostatic Strength: No rupture or burst during 100 hours test at 20 deg C at 12.4 MPa induced hoop stress, and 165 hours test at 80 deg C.
- Melt Flow Rate (MFR): Between 0.2 and 1.4 g/10 min at 190 deg C / 5 kg load.
- Pipes must possess mandatory BIS ISI certification as per the DPIIT Polyethylene Material Quality Control Order.
""",
        "formats": ["txt", "pdf"]
    },
    {
        "id": "08_electrical_pvc_armoured_cables_biased",
        "title": "Supply of Low Voltage PVC Insulated Armoured Power Cables",
        "dept": "Delhi Metro Rail Corporation (DMRC) - Traction & Power",
        "tender_no": "DMRC/ELECT/LV-CABLE/2026/55",
        "text": """DELHI METRO RAIL CORPORATION LIMITED
Tender Notification: DMRC/ELECT/LV-CABLE/2026/55
Works: Station Auxiliary Power Distribution Electrical Cabling

TECHNICAL SPECIFICATION:

1. ITEM PARTICULARS:
Supply of 1100 Volts (1.1 kV) Grade Heavy Duty Cross-Linked/PVC Insulated Aluminium Conductor Armoured Underground Power Cables.

2. BRAND COMPLIANCE REQUIREMENT:
The cables must be manufactured exclusively by Havells or Polycab or Finolex. Equipment from other manufacturers will not qualify for technical evaluation.

3. DESIGN AND CONSTRUCTION PARAMETERS:
- System Voltage: Rated for 1100 V AC, 3-Phase 50 Hz earthed / unearthed electrical system.
- Size and Core Configuration: 4-Core x 25 sq. mm.
- Conductor: Stranded compact shaped H4 grade EC Aluminium complying with Class 2 flexibility.
- Insulation: Type A PVC compound extruded over conductors.
- Inner Sheath: Extruded PVC matching Type ST1.
- Armouring: Single layer of Galvanized Round Steel Wire / Formed Steel Strip providing minimum 90% surface coverage.
- Outer Sheath: Heavy-duty extruded PVC compound Type ST1, flame retardant (FR) with oxygen index >= 29%.
- Statutory Markings: Mandatory ISI embossing with manufacturer license code under the Electrical Wires and Cable QCO.
""",
        "formats": ["txt", "docx"]
    },
    {
        "id": "09_electrical_solar_grid_inverter",
        "title": "Procurement of 50 kW Grid-Tied Solar Photovoltaic Inverters for Govt Rooftops",
        "dept": "Ministry of New and Renewable Energy (MNRE) - Grid Solar Division",
        "tender_no": "MNRE/SOLAR/INV-50KW/2026/303",
        "text": """MINISTRY OF NEW AND RENEWABLE ENERGY
Tender Notice: MNRE/SOLAR/INV-50KW/2026/303
Scheme: Solarization of Government Buildings and Educational Campuses

TECHNICAL SPECIFICATION SCHEDULE:

1. EQUIPMENT PURPOSE:
Three-phase transformerless grid-tied solar photovoltaic string inverters for conversion of DC energy generated by rooftop solar arrays into synchronized AC grid power.

2. TECHNICAL SPECIFICATIONS:
- Nominal AC Power Output: 50 kW at 415 V (+/- 10%), 3-phase, 4-wire, 50 Hz (+/- 3 Hz).
- Maximum DC Input Voltage: 1100 V DC.
- MPPT Operating Voltage Range: 200 V to 1000 V DC with at least 2 independent MPPT trackers.
- Peak Inverter Efficiency: Greater than 98.5%; Euro Efficiency > 98.0%.
- Total Harmonic Distortion (THD): Less than 3.0% at rated output.
- Power Factor: Adjustable between 0.8 leading to 0.8 lagging (nominal > 0.99).
- Protection Features: Anti-islanding protection (under-voltage, over-voltage, under-frequency, over-frequency), DC reverse polarity, AC short circuit, and Type II surge arresters.
- Ingress Protection: IP65 enclosure for outdoor weatherproofing.
- Certification: Mandatory compliance with MeitY / MNRE Solar Photovoltaics Quality Control Order (CRO registration).
""",
        "formats": ["txt"]
    },
    {
        "id": "10_safety_industrial_helmets_qco",
        "title": "Supply of Industrial Safety Helmets for Tunnel Boring Project Workers",
        "dept": "Border Roads Organisation (BRO) - Strategic Tunnel Construction Unit",
        "tender_no": "BRO/TUNNEL/PPE-HELMET/2026/12",
        "text": """BORDER ROADS ORGANISATION - MINISTRY OF DEFENCE
NIT Reference: BRO/TUNNEL/PPE-HELMET/2026/12
Project: Rohtang Bypass and High-Altitude Tunnel Works

TECHNICAL SPECIFICATIONS - PERSONAL PROTECTIVE EQUIPMENT (PPE):

1. ITEM SPECIFICATION:
Supply of Non-Metallic Industrial Safety Helmets with 4-point harness and sweatband for construction workers, miners, and engineers exposed to falling objects and electrical shock hazards.

2. APPROVED MAKES AND BRANDS:
Helmets shall be procured from reputed safety brands such as Karam or 3M or Karam Safety. Alternate local makes must demonstrate equivalent certification.

3. PERFORMANCE AND TEST REQUIREMENTS:
- Shell Material: High density virgin polymer (HDPE/ABS) resistant to impact, puncture, and UV degradation.
- Shock Absorption: Transmitted force through the helmet shell to the headform shall not exceed 5.0 kN when subjected to 5 kg falling striker drop test from 1.0 meter height.
- Penetration Resistance: Conical striker dropped from 1.0 m shall not make contact with headform.
- Electrical Insulation: Shell shall withstand high-voltage electrical breakdown test of 2000 Volts AC leakage current <= 3 mA.
- Flame Resistance: Shell material shall not continue burning for more than 5 seconds after burner flame removal.
- Chin Strap Retention: Chin strap with minimum 19 mm width with breaking load between 150 N and 250 N.
- Regulatory Mandate: Helmets must bear mandatory ISI Mark under the Personal Protective Equipment Quality Control Order issued by DPIIT.
""",
        "formats": ["txt", "pdf"]
    },
    {
        "id": "11_safety_n95_respiratory_masks",
        "title": "Procurement of Particulate Respirator Face Masks (N95 / FFP2) for Hospitals",
        "dept": "All India Institute of Medical Sciences (AIIMS) - Hospital Stores",
        "tender_no": "AIIMS/PROC/COVID-PPE/2026/41",
        "text": """ALL INDIA INSTITUTE OF MEDICAL SCIENCES
Tender Reference: AIIMS/PROC/COVID-PPE/2026/41
Division: Central Hospital Stores - Emergency Infection Control

TECHNICAL REQUIREMENTS:

1. SCOPE:
Supply of particulate filtering half masks (respiratory protective devices) without exhalation valve for clinical staff dealing with airborne aerosol pathogens and fine particulates.

2. FUNCTIONAL CRITERIA:
- Particle Filtration Efficiency: Minimum 95.0% against Sodium Chloride (NaCl) solid aerosols and paraffin oil mist at test flow rate of 95 Litres/minute.
- Total Inward Leakage (TIL): Shall not exceed 8% of the inhalation air.
- Breathing Resistance:
  * Inhalation at 30 L/min: Maximum 70 Pa
  * Inhalation at 95 L/min: Maximum 240 Pa
  * Exhalation at 160 L/min: Maximum 300 Pa
- Fluid Splash Resistance: Minimum synthetic blood penetration resistance at 120 mm Hg pressure.
- Fit and Fastening: Dual synthetic elastic headbands (not ear loops) providing uniform seal tension; adjustable aluminium nose clip with internal soft foam padding.
- Standard Conformity: Mask must be certified under the Indian Standard for Respiratory Protective Devices.
""",
        "formats": ["txt"]
    },
    {
        "id": "12_it_laptops_brand_biased_dell",
        "title": "Supply of Executive Laptops for State Secretariat Departments",
        "dept": "State Department of Information Technology & e-Governance",
        "tender_no": "DIT/EGOV/LAPTOP-OFFICE/2026/89",
        "text": """DEPARTMENT OF INFORMATION TECHNOLOGY AND E-GOVERNANCE
Bid Reference: DIT/EGOV/LAPTOP-OFFICE/2026/89
Subject: Supply of Executive Laptops for Senior Administrative Officers

TECHNICAL SCHEDULE & ELIGIBILITY TERMS:

1. MANDATORY PRODUCT SELECTION:
Bidders must offer and deliver only Dell Latitude 5440 or HP EliteBook 840 G10 laptops. Any offer proposing alternative manufacturers such as Acer, Asus, Lenovo, or local brands will be disqualified at technical scrutiny without evaluation.

2. HARDWARE SPECIFICATIONS:
- Processor: Intel Core i7 13th Generation (10 cores, up to 5.0 GHz turbo frequency) or Apple M2.
- Memory: 16 GB DDR5 RAM (expandable up to 64 GB).
- Storage: 512 GB M.2 NVMe PCIe Gen 4 High Speed Solid State Drive (SSD).
- Display: 14.0 inch Full HD (1920 x 1080) anti-glare IPS display with minimum 300 nits brightness.
- Ports: At least 2x Thunderbolt 4 / USB-C, 2x USB 3.2 Gen 1, 1x HDMI 2.0, 1x RJ45 Gigabit Ethernet.
- Wireless: Wi-Fi 6E (802.11ax) and Bluetooth 5.3.
- Operating System: Windows 11 Pro 64-bit pre-activated with recovery media.
- Safety & Registration: Laptop and power adapter must have valid registration under the Compulsory Registration Scheme (CRS) of MeitY for Electronic and IT Goods.
""",
        "formats": ["txt", "docx"]
    },
    {
        "id": "13_mechanical_centrifugal_pump",
        "title": "Procurement of Horizontal End Suction Centrifugal Pumps for Water Works",
        "dept": "Urban Water Supply and Sewerage Board",
        "tender_no": "UWSSB/MECH/PUMP-WATER/2026/19",
        "text": """MUNICIPAL WATER SUPPLY AND SEWERAGE BOARD
Tender Notice No: UWSSB/MECH/PUMP-WATER/2026/19
Project: Augmentation of Clear Water Pumping Station at Sector 4

SCHEDULE OF TECHNICAL SPECIFICATIONS:

1. EQUIPMENT DETAILS:
Supply, testing, and delivery of horizontal end-suction back pull-out centrifugal water pumps driven by continuous duty squirrel cage induction motors.

2. OPERATING DUTY PARAMETERS:
- Handled Liquid: Clear, potable drinking water at ambient temperature (5 to 45 deg C).
- Rated Discharge Capacity: 150 cubic meters per hour (m3/hr).
- Total Dynamic Head (TDH): 45.0 meters at rated discharge.
- Pump Speed: 1450 RPM synchronous speed.
- Minimum Pump Efficiency at Best Efficiency Point (BEP): 78.0%.
- Motor Rating: 30 kW, 415 V (+/- 10%), 3-Phase, 50 Hz, TEFC enclosure, IP55 protection, Class F insulation.

3. MATERIAL OF CONSTRUCTION:
- Pump Casing: Heavy duty Cast Iron FG 200 / FG 260 with minimum corrosion allowance 3 mm.
- Impeller: Phosphor Bronze or Stainless Steel Grade CF8M dynamically balanced.
- Pump Shaft: High tensile stainless steel Grade AISI 410.
- Shaft Sealing: Mechanical seal with silicon carbide faces.
- Standards Conformity: Designed and tested strictly in compliance with Indian Standard for Centrifugal Pumps.
""",
        "formats": ["txt"]
    },
    {
        "id": "14_textiles_cotton_hospital_bedsheets",
        "title": "Supply of Bleached Cotton Bed Sheets for Government Hospital Wards",
        "dept": "Directorate General of Health Services (DGHS) - Central Medical Stores",
        "tender_no": "DGHS/MED/TEXTILE-BED/2026/62",
        "text": """DIRECTORATE GENERAL OF HEALTH SERVICES
Tender Ref No: DGHS/MED/TEXTILE-BED/2026/62
Procurement Unit: Central Medical Stores - Hospital Linen Division

SPECIFICATIONS FOR COTTON BED SHEETS:

1. ITEM SPECIFICATION:
Supply of 100% Cotton Bleached Hospital Bed Sheets for patient beds across civil and district government hospitals.

2. DIMENSIONAL AND MATERIAL PROPERTIES:
- Fiber Composition: 100% pure combed virgin cotton, free from synthetic or recycled fibers.
- Dimensions: Length 230 cm (+/- 2 cm) x Width 150 cm (+/- 2 cm).
- Weave: Plain woven fabric with balanced construction.
- Thread Count: Minimum 180 Threads per Square Inch (Warp 30s count, Weft 30s count).
- Mass per Unit Area (GSM): Minimum 140 grams/m2.
- Breaking Strength:
  * Warp Direction: Minimum 350 N.
  * Weft Direction: Minimum 300 N.
- Bleaching and Whiteness: Fully bleached to minimum 80% whiteness index on Hunter scale, free from optical brightening agent streaks.
- Dimensional Shrinkage: Not more than 3.0% in warp and 2.0% in weft after standard boiling wash.
- Color Fastness: Fastness to repeated washing rating 4 or higher.
""",
        "formats": ["txt"]
    }
]

def create_pdf(filepath: str, item: dict):
    doc = fitz.open()
    # A4 dimensions: 595 x 842 points
    page = doc.new_page(width=595, height=842)
    
    # Margin and initial position
    margin = 50
    y = 50
    line_height = 14
    
    # Header banner
    rect = fitz.Rect(margin, y, 595 - margin, y + 50)
    page.draw_rect(rect, color=(0.1, 0.3, 0.6), fill=(0.93, 0.95, 0.98), width=1.5)
    
    page.insert_text(fitz.Point(margin + 10, y + 20), "GOVERNMENT PROCUREMENT TENDER SPECIFICATION", fontsize=11, fontname="helv", color=(0.1, 0.3, 0.6))
    page.insert_text(fitz.Point(margin + 10, y + 38), f"Tender Ref: {item.get('tender_no', 'N/A')}  |  Dept: {item.get('dept', '')[:45]}", fontsize=9, fontname="helv", color=(0.2, 0.2, 0.2))
    
    y += 75
    page.insert_text(fitz.Point(margin, y), item["title"], fontsize=13, fontname="helv", color=(0, 0, 0))
    y += 25
    
    # Insert tender text lines
    for line in item["text"].splitlines():
        if y > 780:
            page = doc.new_page(width=595, height=842)
            y = 50
        
        trimmed = line.strip()
        if not trimmed:
            y += line_height // 2
            continue
            
        is_heading = trimmed.isupper() or trimmed.endswith(":") or trimmed.startswith("1.") or trimmed.startswith("2.") or trimmed.startswith("3.")
        fontname = "helv"
        fontsize = 10 if not is_heading else 10.5
        color = (0.1, 0.2, 0.4) if is_heading else (0.15, 0.15, 0.15)
        
        # Word wrap simply
        max_chars = 75
        while len(line) > max_chars:
            split_idx = line.rfind(" ", 0, max_chars)
            if split_idx == -1:
                split_idx = max_chars
            chunk = line[:split_idx]
            line = line[split_idx:].strip()
            page.insert_text(fitz.Point(margin, y), chunk, fontsize=fontsize, fontname=fontname, color=color)
            y += line_height
            if y > 780:
                page = doc.new_page(width=595, height=842)
                y = 50
                
        if line:
            page.insert_text(fitz.Point(margin, y), line, fontsize=fontsize, fontname=fontname, color=color)
            y += line_height
            
    doc.save(filepath)
    doc.close()

def create_docx(filepath: str, item: dict):
    doc = docx.Document()
    
    # Title
    p_title = doc.add_paragraph()
    run_title = p_title.add_run(item["title"])
    run_title.font.size = Pt(14)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(16, 44, 87)
    
    # Metadata
    p_meta = doc.add_paragraph()
    run_meta = p_meta.add_run(f"Tender Ref: {item.get('tender_no', 'N/A')} | Issuing Dept: {item.get('dept', '')}")
    run_meta.font.size = Pt(10)
    run_meta.font.italic = True
    run_meta.font.color.rgb = RGBColor(100, 100, 100)
    
    # Content
    for line in item["text"].splitlines():
        trimmed = line.strip()
        if not trimmed:
            continue
        p = doc.add_paragraph()
        if trimmed.startswith("1.") or trimmed.startswith("2.") or trimmed.startswith("3.") or "SCHEDULE" in trimmed or "SPECIFICATION" in trimmed:
            run = p.add_run(trimmed)
            run.bold = True
            run.font.size = Pt(11)
            run.font.color.rgb = RGBColor(20, 50, 100)
        elif trimmed.startswith("- ") or trimmed.startswith("* "):
            p.paragraph_format.left_indent = Inches(0.25)
            run = p.add_run(trimmed)
            run.font.size = Pt(10)
        else:
            run = p.add_run(trimmed)
            run.font.size = Pt(10)
            
    doc.save(filepath)

def generate_all():
    generated_files = []
    
    for item in SAMPLES:
        item_id = item["id"]
        formats = item.get("formats", ["txt"])
        
        # Always write .txt
        txt_path = os.path.join(SAMPLE_DIR, f"{item_id}.txt")
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(f"TENDER: {item['title']}\n")
            f.write(f"REFERENCE: {item.get('tender_no', 'N/A')}\n")
            f.write(f"DEPARTMENT: {item.get('dept', 'N/A')}\n\n")
            f.write(item["text"])
        generated_files.append(f"{item_id}.txt")
        
        # Write PDF if requested
        if "pdf" in formats:
            pdf_path = os.path.join(SAMPLE_DIR, f"{item_id}.pdf")
            create_pdf(pdf_path, item)
            generated_files.append(f"{item_id}.pdf")
            
        # Write DOCX if requested
        if "docx" in formats:
            docx_path = os.path.join(SAMPLE_DIR, f"{item_id}.docx")
            create_docx(docx_path, item)
            generated_files.append(f"{item_id}.docx")
            
    # Also generate a comprehensive README.md in sample_files
    readme_path = os.path.join(SAMPLE_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("# Sample Procurement Tenders Catalog (SIH-108 Testing Suite)\n\n")
        f.write("This directory contains **14 diverse, realistic Indian public procurement tender specifications** ")
        f.write("covering multiple sectors, departments, and file formats (`.txt`, `.pdf`, `.docx`).\n\n")
        f.write("You can test the engine by:\n")
        f.write("1. **Drag-and-Drop or File Upload:** Drag any `.pdf`, `.docx`, or `.txt` file into the upload zone on the web dashboard at `http://127.0.0.1:8000`.\n")
        f.write("2. **Copy & Paste:** Open any `.txt` file, copy the content, and paste it into the tender specification textarea.\n")
        f.write("3. **CLI / API:** Send the file via `curl` or Python requests to `/api/v1/analyze-file`.\n\n")
        f.write("## Test Cases Overview\n\n")
        f.write("| # | File Name | Formats | Sector / Ministry | Key Features & Test Objective | Expected BIS Standard | Compliance Alerts |\n")
        f.write("|---|-----------|---------|-------------------|--------------------------------|-----------------------|-------------------|\n")
        f.write("| 1 | `01_food_fortified_rice_frk` | `.txt`, `.pdf` | Food & Public Distribution (DFPD/FCI) | Fortified Rice Kernels, Iron, Folic Acid, B12 micronutrients | **IS 17782** | Clean / No Bias |\n")
        f.write("| 2 | `02_food_pds_wheat_atta_biased` | `.txt`, `.docx` | Food & Civil Supplies | Brand Bias (`Aashirvaad`, `Fortune`), Chakki atta parameters | **IS 1155** | GFR 144(i) Bias Detected & Auto-Sanitized |\n")
        f.write("| 3 | `03_food_jute_bags_50kg_fci` | `.txt`, `.pdf` | Foodgrain Packaging (FCI) | 50kg Twill Jute Bags, dimensions, tensile breaking strength | **IS 12650** | Clean / No Bias |\n")
        f.write("| 4 | `04_food_packaged_drinking_water_biased` | `.txt` | IRCTC / Food Safety | Brand Bias (`Bisleri`, `Aquafina`, `Kinley`), TDS, RO | **IS 14543** | Brand Bias + Mandatory QCO Alert |\n")
        f.write("| 5 | `05_civil_flyover_tmt_rebars_obsolete_biased` | `.txt`, `.pdf` | Civil Infrastructure (CPWD) | Obsolete `IS 1139` + Brand Bias (`Tata Tiscon`, `Jindal Panther`) | **IS 1786** | Obsolete Standard Replaced + Steel QCO |\n")
        f.write("| 6 | `06_civil_ppc_cement_biased` | `.txt`, `.docx` | Highway Engineering (NHAI) | Brand Bias (`UltraTech`, `ACC`, `Ambuja`), Flyash PPC | **IS 1489 Part 1** | Brand Bias + Cement Mandatory QCO |\n")
        f.write("| 7 | `07_civil_hdpe_water_pipes_jjm` | `.txt`, `.pdf` | Water Infrastructure (Jal Jeevan) | PE 100, PN 10, 110mm outer diameter HDPE pipes | **IS 4984** | Mandatory Polyethylene QCO Alert |\n")
        f.write("| 8 | `08_electrical_pvc_armoured_cables_biased` | `.txt`, `.docx` | Metro Rail Electrical (DMRC) | Brand Bias (`Havells`, `Polycab`, `Finolex`), 1.1kV 4-core | **IS 1554 Part 1** | Brand Bias + Electrical Cable QCO |\n")
        f.write("| 9 | `09_electrical_solar_grid_inverter` | `.txt` | Renewable Energy (MNRE/SECI) | 50 kW 3-phase grid-tied string inverter, THD < 3%, MPPT | **IS 16221 Part 2** | Mandatory MeitY/MNRE CRO Order |\n")
        f.write("| 10 | `10_safety_industrial_helmets_qco` | `.txt`, `.pdf` | Personal Protective Equipment (BRO) | Brand Bias (`3M`, `Karam`), 5.0 kN shock absorption | **IS 2925** | Brand Bias + Mandatory PPE QCO |\n")
        f.write("| 11 | `11_safety_n95_respiratory_masks` | `.txt` | Healthcare PPE (AIIMS) | N95 / FFP2 particulate respirator, 95% PFE, breathing resistance | **IS 9473** | Respiratory PPE Standard |\n")
        f.write("| 12 | `12_it_laptops_brand_biased_dell` | `.txt`, `.docx` | IT & e-Governance | Restrictive Single-Vendor Bias (`Dell Latitude`, `HP EliteBook`) | **IS 13252 Part 1** | GFR 144(i) Brand Struck Out + MeitY CRO |\n")
        f.write("| 13 | `13_mechanical_centrifugal_pump` | `.txt` | Municipal Waterworks | 150 m3/hr, 45m head, 30 kW motor end-suction pump | **IS 1520** | Mechanical Pump Performance Standard |\n")
        f.write("| 14 | `14_textiles_cotton_hospital_bedsheets` | `.txt` | Medical Linen (DGHS) | 100% cotton, 230x150 cm, 180 TC, 140 GSM bedsheets | **IS 745** | Textile Strength & Fastness Standard |\n")

    print(f"Successfully generated {len(generated_files)} sample tender files and README.md in {SAMPLE_DIR}")
    for gf in sorted(generated_files):
        print(f"  - {gf}")

if __name__ == "__main__":
    generate_all()
