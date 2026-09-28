import json
from pathlib import Path

null = None
false = False
true = True

BASE_DIR = Path(__file__).resolve().parent.parent
CATALOG_PATH = BASE_DIR / "data" / "standards_catalog.json"

# Load existing 22 standards
with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    existing_standards = json.load(f)

# Existing IS codes set
existing_codes = set(s["base_code"] for s in existing_standards)

# New standards to add across all 14 Division Councils
new_standards = [
    # --- CED (Civil Engineering) ---
    {
        "is_code": "IS 383:2016",
        "base_code": "IS 383",
        "part": null,
        "title": "Coarse and Fine Aggregate for Concrete - Specification",
        "publication_year": 2016,
        "reaffirmed_year": 2021,
        "edition": "Third Revision",
        "division_code": "CED",
        "division_name": "Civil Engineering Division",
        "sectional_committee": "CED 2 (Cement and Concrete)",
        "status": "ACTIVE",
        "supersedes": ["IS 383:1970"],
        "superseded_by": null,
        "mandatory_qco": false,
        "qco_ministry": null,
        "qco_order_name": null,
        "scope": "Covers chemical and physical requirements and methods of test for coarse aggregate, fine aggregate (natural sand, crushed stone sand, manufactured sand), and all-in aggregate for use in concrete.",
        "keywords": ["coarse aggregate", "fine aggregate", "sand", "gravel", "crushed stone", "m-sand", "manufactured sand", "grading zone", "flakiness index", "elongation index", "crushing value"],
        "clauses": [
            {
                "clause_number": "Clause 4.1",
                "clause_title": "Types of Aggregates",
                "content": "Aggregates are classified into Natural Aggregate, Manufactured Aggregate (M-Sand), and Recycled Concrete Aggregate (RCA)."
            },
            {
                "clause_number": "Table 2",
                "clause_title": "Grading Limits for Fine Aggregates",
                "content": "Specifies passing percentages for 4.75mm, 2.36mm, 1.18mm, 600 micron, 300 micron, and 150 micron across Grading Zones I, II, III, and IV."
            }
        ]
    },
    {
        "is_code": "IS 800:2007",
        "base_code": "IS 800",
        "part": null,
        "title": "General Construction in Steel - Code of Practice",
        "publication_year": 2007,
        "reaffirmed_year": 2022,
        "edition": "Third Revision",
        "division_code": "CED",
        "division_name": "Civil Engineering Division",
        "sectional_committee": "CED 7 (Structural Engineering and Structural Sections)",
        "status": "ACTIVE",
        "supersedes": ["IS 800:1984"],
        "superseded_by": null,
        "mandatory_qco": false,
        "qco_ministry": null,
        "qco_order_name": null,
        "scope": "Provides criteria for design and construction of steel structures using Limit State Method (LSM) for hot rolled steel sections and plate girders in industrial buildings, bridges, and infrastructure.",
        "keywords": ["structural steel design", "steel construction", "limit state design", "bolted connections", "welded connections", "girders", "trusses", "buckling", "deflection limit"],
        "clauses": [
            {
                "clause_number": "Clause 5.1",
                "clause_title": "Design Principles",
                "content": "Structures shall be designed by limit state method for Limit State of Strength and Limit State of Serviceability."
            }
        ]
    },
    {
        "is_code": "IS 4984:2016",
        "base_code": "IS 4984",
        "part": null,
        "title": "High Density Polyethylene (HDPE) Pipes for Water Supply - Specification",
        "publication_year": 2016,
        "reaffirmed_year": 2021,
        "edition": "Fifth Revision",
        "division_code": "CED",
        "division_name": "Civil Engineering Division",
        "sectional_committee": "CED 53 (Pipes and Fittings)",
        "status": "ACTIVE",
        "supersedes": ["IS 4984:1995"],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "DPIIT",
        "qco_order_name": "Polyethylene Pipes and Fittings (Quality Control) Order",
        "scope": "Prescribes requirements for high density polyethylene (HDPE) pipes made from PE 63, PE 80, and PE 100 materials for water supply for domestic and industrial purposes.",
        "keywords": ["hdpe pipe", "polyethylene pipe", "pe 100", "pe 80", "water supply pipe", "pn 6", "pn 10", "pn 16", "butt fusion", "electrofusion", "hydrostatic strength"],
        "clauses": [
            {
                "clause_number": "Clause 5.1",
                "clause_title": "Material Designation",
                "content": "Pipes shall be manufactured from carbon black compound PE 63, PE 80, or PE 100 with density >= 940 kg/m3."
            }
        ]
    },
    {
        "is_code": "IS 1536:2001",
        "base_code": "IS 1536",
        "part": null,
        "title": "Centrifugally Cast (Spun) Iron Pressure Pipes for Water, Gas and Sewage - Specification",
        "publication_year": 2001,
        "reaffirmed_year": 2021,
        "edition": "Fourth Revision",
        "division_code": "CED",
        "division_name": "Civil Engineering Division",
        "sectional_committee": "CED 53 (Pipes and Fittings)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "Ministry of Steel",
        "qco_order_name": "Ductile and Cast Iron Pipes QCO",
        "scope": "Covers centrifugally cast ductile and grey iron pressure pipes with socket and spigot ends or flanged ends for transmitting water, gas and sewage.",
        "keywords": ["di pipe", "ductile iron pipe", "cast iron pipe", "spun pipe", "water mains", "sewage pipe", "socket and spigot", "k9 pipe", "k7 pipe", "hydrostatic test"],
        "clauses": [
            {
                "clause_number": "Clause 4.1",
                "clause_title": "Classification",
                "content": "Pipes classified into Class K7, K9, and K12 based on wall thickness and working pressure."
            }
        ]
    },

    # --- ETD (Electrotechnical Division) ---
    {
        "is_code": "IS 7098 (Part 1):1988",
        "base_code": "IS 7098",
        "part": "Part 1",
        "title": "Crosslinked Polyethylene (XLPE) Insulated PVC Sheathed Cables - Specification - Part 1: For Working Voltage Up to and Including 1100 V",
        "publication_year": 1988,
        "reaffirmed_year": 2020,
        "edition": "Second Revision",
        "division_code": "ETD",
        "division_name": "Electrotechnical Division",
        "sectional_committee": "ETD 9 (Cables and Wires)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "DPIIT",
        "qco_order_name": "Cables (Quality Control) Order, 2023",
        "scope": "Specifies requirements for crosslinked polyethylene (XLPE) insulated and PVC sheathed armored and unarmored power cables for voltages up to 1100 V.",
        "keywords": ["xlpe cable", "armoured cable", "power distribution", "copper conductor", "aluminium conductor", "crosslinked polyethylene", "90 deg operating temp"],
        "clauses": [
            {
                "clause_number": "Clause 5.1",
                "clause_title": "Conductor",
                "content": "Conductors shall be Class 2 stranded aluminum or copper conforming to IS 8130."
            },
            {
                "clause_number": "Clause 6.1",
                "clause_title": "Insulation",
                "content": "Insulation shall be cross-linked polyethylene (XLPE) applied by extrusion, rated for 90 deg C continuous operating temperature."
            }
        ]
    },
    {
        "is_code": "IS 7098 (Part 2):2011",
        "base_code": "IS 7098",
        "part": "Part 2",
        "title": "Crosslinked Polyethylene Insulated Thermoplastic Sheathed Cables - Part 2: For Working Voltages From 3.3 kV Up to and Including 33 kV",
        "publication_year": 2011,
        "reaffirmed_year": 2021,
        "edition": "Second Revision",
        "division_code": "ETD",
        "division_name": "Electrotechnical Division",
        "sectional_committee": "ETD 9 (Cables and Wires)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "DPIIT",
        "qco_order_name": "Cables (Quality Control) Order, 2023",
        "scope": "Specifies requirements for XLPE insulated, screened, armored, and sheathed high voltage power cables from 3.3 kV up to 33 kV used in electrical distribution sub-stations.",
        "keywords": ["ht cable", "high tension cable", "11 kv cable", "33 kv cable", "substation cable", "xlpe high voltage", "screened cable", "partial discharge test"],
        "clauses": [
            {
                "clause_number": "Clause 14.1",
                "clause_title": "Partial Discharge Test",
                "content": "Partial discharge magnitude at 1.5 U0 shall not exceed 5 pC."
            }
        ]
    },
    {
        "is_code": "IS 1180 (Part 1):2014",
        "base_code": "IS 1180",
        "part": "Part 1",
        "title": "Outdoor Type Oil-Immersed Distribution Transformers Up to and Including 2500 kVA, 33 kV - Specification",
        "publication_year": 2014,
        "reaffirmed_year": 2021,
        "edition": "Fourth Revision",
        "division_code": "ETD",
        "division_name": "Electrotechnical Division",
        "sectional_committee": "ETD 16 (Transformers)",
        "status": "ACTIVE",
        "supersedes": ["IS 1180 (Part 1):1989"],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "Ministry of Power / DPIIT",
        "qco_order_name": "Distribution Transformers (Quality Control) Order",
        "scope": "Covers outdoor type oil immersed distribution transformers up to 2500 kVA and 33 kV with standard energy efficiency star ratings (Energy Level 1, 2, and 3).",
        "keywords": ["transformer", "distribution transformer", "100 kva transformer", "250 kva", "oil immersed", "bee star rating", "energy efficient transformer", "discom procurement"],
        "clauses": [
            {
                "clause_number": "Table 3",
                "clause_title": "Maximum Total Losses",
                "content": "Specifies maximum total losses at 50% and 100% loading for Energy Level 1, 2, and 3 to ensure BEE energy efficiency compliance."
            }
        ]
    },
    {
        "is_code": "IS 8828:1996",
        "base_code": "IS 8828",
        "part": null,
        "title": "Electrical Accessories - Circuit-Breakers for Overcurrent Protection for Household and Similar Installations (MCBs)",
        "publication_year": 1996,
        "reaffirmed_year": 2021,
        "edition": "Second Revision",
        "division_code": "ETD",
        "division_name": "Electrotechnical Division",
        "sectional_committee": "ETD 14 (Electrical Accessories)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "DPIIT",
        "qco_order_name": "Circuit Breakers (Quality Control) Order",
        "scope": "Applies to AC air-break miniature circuit-breakers (MCBs) for operation at 50 Hz, with rated voltage <= 440 V and rated current <= 125 A, with rated breaking capacity up to 10,000 A.",
        "keywords": ["mcb", "miniature circuit breaker", "circuit breaker", "overcurrent protection", "short circuit protection", "10ka mcb", "c curve", "b curve", "distribution board"],
        "clauses": [
            {
                "clause_number": "Clause 5.2",
                "clause_title": "Tripping Characteristics",
                "content": "Standard instantaneous tripping curves designated as Type B (3 In to 5 In), Type C (5 In to 10 In), and Type D (10 In to 20 In)."
            }
        ]
    },
    {
        "is_code": "IS 16221 (Part 2):2015",
        "base_code": "IS 16221",
        "part": "Part 2",
        "title": "Safety of Power Converters for Use in Photovoltaic Power Systems - Part 2: Particular Requirements for Inverters",
        "publication_year": 2015,
        "reaffirmed_year": 2020,
        "edition": "First Edition",
        "division_code": "ETD",
        "division_name": "Electrotechnical Division",
        "sectional_committee": "ETD 28 (Solar Photovoltaic Energy Systems)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "Ministry of New and Renewable Energy (MNRE)",
        "qco_order_name": "Solar Photovoltaics, Systems, Devices and Components Goods (Requirements for Compulsory Registration) Order",
        "scope": "Provides safety requirements for grid-connected and off-grid utility-interconnected solar photovoltaic inverters converting DC solar array power to AC electricity.",
        "keywords": ["solar inverter", "pv inverter", "photovoltaic power converter", "grid tied inverter", "mnre", "solar power plant", "anti-islanding", "solar rooftop"],
        "clauses": [
            {
                "clause_number": "Clause 4.1",
                "clause_title": "Anti-Islanding Protection",
                "content": "Grid-connected solar inverters must automatically disconnect within 2 seconds upon loss of main grid power to prevent hazardous islanding."
            }
        ]
    },
    {
        "is_code": "IS 16102 (Part 1):2012",
        "base_code": "IS 16102",
        "part": "Part 1",
        "title": "Self-Ballasted LED Lamps for General Lighting Services - Part 1: Safety Requirements",
        "publication_year": 2012,
        "reaffirmed_year": 2021,
        "edition": "First Edition",
        "division_code": "ETD",
        "division_name": "Electrotechnical Division",
        "sectional_committee": "ETD 23 (Electric Lamps and Accessories)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "MeitY / DPIIT",
        "qco_order_name": "Compulsory Registration Scheme for LED Lighting",
        "scope": "Specifies safety and interchangeability requirements for self-ballasted LED lamps for domestic and similar general lighting services with rated wattage up to 60 W and voltage up to 250 V.",
        "keywords": ["led lamp", "led bulb", "b22 cap", "e27 cap", "energy saving bulb", "luminaire", "lighting safety", "meity crs"],
        "clauses": [
            {
                "clause_number": "Clause 6.1",
                "clause_title": "Insulation Resistance and Electric Strength",
                "content": "Insulation resistance shall not be less than 4 MOhm, and lamp must withstand high voltage dielectric test."
            }
        ]
    },

    # --- LITD (Electronics and Information Technology Division) ---
    {
        "is_code": "IS 13252 (Part 1):2010",
        "base_code": "IS 13252",
        "part": "Part 1",
        "title": "Information Technology Equipment - Safety - General Requirements",
        "publication_year": 2010,
        "reaffirmed_year": 2020,
        "edition": "Second Edition",
        "division_code": "LITD",
        "division_name": "Electronics & IT Division",
        "sectional_committee": "LITD 8 (Information Technology Hardware)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "MeitY",
        "qco_order_name": "Electronics and Information Technology Goods Compulsory Registration Order",
        "scope": "Applies to mains-powered or battery-powered information technology equipment, including personal computers, laptops, servers, printers, displays, scanners, and data storage systems.",
        "keywords": ["computer safety", "laptop", "server", "printer", "it hardware", "desktop pc", "meity registration", "crs registration", "electrical safety for computers"],
        "clauses": [
            {
                "clause_number": "Clause 1.5",
                "clause_title": "Components Protection",
                "content": "Components such as power supply modules, capacitors, and transformers must meet fire hazard and thermal limits."
            }
        ]
    },
    {
        "is_code": "IS 16333 (Part 3):2022",
        "base_code": "IS 16333",
        "part": "Part 3",
        "title": "Mobile Phone Handsets - Part 3: Language Support for Indian Languages",
        "publication_year": 2022,
        "reaffirmed_year": null,
        "edition": "Second Revision",
        "division_code": "LITD",
        "division_name": "Electronics & IT Division",
        "sectional_committee": "LITD 13 (Telecommunications)",
        "status": "ACTIVE",
        "supersedes": ["IS 16333 (Part 3):2016"],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "MeitY",
        "qco_order_name": "Indian Language Support for Mobile Handsets Mandate",
        "scope": "Specifies Indian language support requirements for all mobile phone handsets sold or procured in India, mandating display and input support for all 22 official Indian languages.",
        "keywords": ["mobile phone", "smartphone", "indian language support", "devanagari", "meity smartphone mandate", "sar value", "handset procurement"],
        "clauses": [
            {
                "clause_number": "Clause 4.1",
                "clause_title": "Mandatory Script Display",
                "content": "Handset must render message reading and text entry in English, Hindi, and at least one official regional language."
            }
        ]
    },

    # --- MED (Mechanical Engineering Division) ---
    {
        "is_code": "IS 9079:2002",
        "base_code": "IS 9079",
        "part": null,
        "title": "Electric Monobloc Pumpsets for Clear, Cold, Fresh Water - Specification",
        "publication_year": 2002,
        "reaffirmed_year": 2022,
        "edition": "Second Revision",
        "division_code": "MED",
        "division_name": "Mechanical Engineering Division",
        "sectional_committee": "MED 20 (Pumps)",
        "status": "ACTIVE",
        "supersedes": ["IS 9079:1989"],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "Ministry of Heavy Industries",
        "qco_order_name": "Monobloc Pumps Quality Control Order",
        "scope": "Covers electric monobloc centrifugal pumpsets where pump and motor form an integral compact unit for agricultural and drinking water supply with total heads up to 90 meters.",
        "keywords": ["monobloc pump", "agricultural pump", "irrigation pump", "electric pumpset", "domestic water pump", "overall efficiency", "head vs discharge"],
        "clauses": [
            {
                "clause_number": "Clause 8.1",
                "clause_title": "Minimum Efficiency Requirement",
                "content": "Overall efficiency shall comply with prescribed minimum values based on rated power (kW) and specific speed."
            }
        ]
    },
    {
        "is_code": "IS 8034:2002",
        "base_code": "IS 8034",
        "part": null,
        "title": "Submersible Pumpsets for Clear, Cold, Fresh Water - Specification",
        "publication_year": 2002,
        "reaffirmed_year": 2021,
        "edition": "Second Revision",
        "division_code": "MED",
        "division_name": "Mechanical Engineering Division",
        "sectional_committee": "MED 20 (Pumps)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "Ministry of Heavy Industries",
        "qco_order_name": "Submersible Pumps QCO",
        "scope": "Covers design, manufacturing and performance testing of multistage submersible centrifugal pumpsets for deep tube-wells and borewells.",
        "keywords": ["submersible pump", "borewell pump", "deep well pump", "multistage pump", "tube well", "rural water supply", "thrust bearing"],
        "clauses": [
            {
                "clause_number": "Clause 6.1",
                "clause_title": "Hydrostatic Testing",
                "content": "Pump bowl and discharge casing shall withstand test pressure of 1.5 times maximum shut-off head for 5 minutes."
            }
        ]
    },
    {
        "is_code": "IS 2825:1969",
        "base_code": "IS 2825",
        "part": null,
        "title": "Code for Unfired Pressure Vessels",
        "publication_year": 1969,
        "reaffirmed_year": 2021,
        "edition": "First Edition",
        "division_code": "MED",
        "division_name": "Mechanical Engineering Division",
        "sectional_committee": "MED 22 (Pressure Vessels)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "PESO / DPIIT",
        "qco_order_name": "Pressure Vessels Quality Mandate",
        "scope": "Specifies design, material selection, fabrication, inspection and testing of unfired fusion-welded pressure vessels for chemical, petroleum, and power plants.",
        "keywords": ["pressure vessel", "unfired vessel", "boiler alternative", "chemical reactor", "compressed air tank", "storage vessel", "weld joint efficiency", "radiography"],
        "clauses": [
            {
                "clause_number": "Clause 3.1",
                "clause_title": "Vessel Classes",
                "content": "Pressure vessels classified into Class I (fully radiographed), Class II (spot radiographed), and Class III (visual inspection only)."
            }
        ]
    },
    {
        "is_code": "IS 277:2018",
        "base_code": "IS 277",
        "part": null,
        "title": "Galvanized Steel Sheets (Plain and Corrugated) - Specification",
        "publication_year": 2018,
        "reaffirmed_year": 2023,
        "edition": "Seventh Revision",
        "division_code": "MED",
        "division_name": "Mechanical & Materials Division",
        "sectional_committee": "MTD 4 (Wrought Steel)",
        "status": "ACTIVE",
        "supersedes": ["IS 277:2003"],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "Ministry of Steel",
        "qco_order_name": "Steel and Steel Products QCO",
        "scope": "Prescribes requirements for zinc-coated galvanized plain and corrugated steel sheets and coils used for roofing, cladding, and packaging.",
        "keywords": ["galvanized sheets", "gi sheet", "corrugated roofing sheet", "zinc coating", "tin sheet", "roofing shed", "warehouse roof"],
        "clauses": [
            {
                "clause_number": "Clause 6.1",
                "clause_title": "Zinc Coating Mass",
                "content": "Coating designations range from 120 g/m2 up to 450 g/m2 total both sides."
            }
        ]
    },

    # --- PCD (Petroleum, Coal and Related Products Division) ---
    {
        "is_code": "IS 73:2013",
        "base_code": "IS 73",
        "part": null,
        "title": "Paving Bitumen - Specification",
        "publication_year": 2013,
        "reaffirmed_year": 2023,
        "edition": "Fourth Revision",
        "division_code": "PCD",
        "division_name": "Petroleum, Coal and Related Products Division",
        "sectional_committee": "PCD 6 (Bitumen, Tar and Related Products)",
        "status": "ACTIVE",
        "supersedes": ["IS 73:2006"],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "Ministry of Petroleum and Natural Gas",
        "qco_order_name": "Bitumen Quality Control Order",
        "scope": "Covers viscosity graded paving bitumen (VG 10, VG 20, VG 30, VG 40) used in road construction, highway pavements, and airport runways.",
        "keywords": ["bitumen", "tar", "asphalt", "vg 30", "vg 40", "paving bitumen", "highway construction", "viscosity grade", "penetration test", "ductility"],
        "clauses": [
            {
                "clause_number": "Table 1",
                "clause_title": "Requirements for Paving Bitumen",
                "content": "For VG 30: Absolute viscosity at 60 deg C = 2400 to 3600 Poises; Kinematic viscosity at 135 deg C min 350 cSt; Penetration at 25 deg C = 45; Softening point min 47 deg C."
            }
        ]
    },
    {
        "is_code": "IS 1460:2017",
        "base_code": "IS 1460",
        "part": null,
        "title": "Automotive Diesel Fuel - Specification (Bharat Stage VI)",
        "publication_year": 2017,
        "reaffirmed_year": 2022,
        "edition": "Sixth Revision",
        "division_code": "PCD",
        "division_name": "Petroleum, Coal and Related Products Division",
        "sectional_committee": "PCD 3 (Petroleum Products)",
        "status": "ACTIVE",
        "supersedes": ["IS 1460:2005"],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "Ministry of Petroleum and Natural Gas",
        "qco_order_name": "Automotive Fuels (Quality Standards) Order",
        "scope": "Specifies requirements for high speed diesel (HSD) fuel conforming to Bharat Stage VI (BS-VI) automotive emission norms with ultra-low sulphur content.",
        "keywords": ["diesel", "hsd", "high speed diesel", "bs-vi diesel", "cetane number", "sulphur 10 ppm", "automotive fuel", "transport fuel"],
        "clauses": [
            {
                "clause_number": "Table 1",
                "clause_title": "BS-VI Diesel Requirements",
                "content": "Sulphur content maximum 10 mg/kg (10 ppm); Cetane index minimum 46 (Cetane number min 51); Flash point min 35 deg C; Density at 15 deg C = 820 to 845 kg/m3."
            }
        ]
    },

    # --- MHD (Medical Equipment & Hospital Planning Division) ---
    {
        "is_code": "IS 4148:1989",
        "base_code": "IS 4148",
        "part": null,
        "title": "Surgical Rubber Gloves - Specification",
        "publication_year": 1989,
        "reaffirmed_year": 2020,
        "edition": "Second Revision",
        "division_code": "MHD",
        "division_name": "Medical Equipment & Hospital Planning Division",
        "sectional_committee": "MHD 12 (Hospital Equipment and Surgical Supplies)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "Ministry of Health and Family Welfare / CDSCO",
        "qco_order_name": "Medical Devices (Quality and Safety) Rules",
        "scope": "Specifies dimensions, tensile strength, elongation, pinhole freedom and water tightness requirements for sterile, packaged disposable surgical rubber gloves.",
        "keywords": ["surgical gloves", "rubber gloves", "latex gloves", "sterile gloves", "hospital gloves", "medical supplies", "pinhole test", "tensile strength"],
        "clauses": [
            {
                "clause_number": "Clause 4.1",
                "clause_title": "Tensile Properties",
                "content": "Tensile strength before accelerated aging shall not be less than 24.0 MPa; Ultimate elongation min 750%."
            }
        ]
    },
    {
        "is_code": "IS 10245 (Part 2):1994",
        "base_code": "IS 10245",
        "part": "Part 2",
        "title": "Breathing Apparatus - Specification - Part 2: Open Circuit Self-Contained Compressed Air Breathing Apparatus",
        "publication_year": 1994,
        "reaffirmed_year": 2020,
        "edition": "First Revision",
        "division_code": "MHD",
        "division_name": "Medical Equipment & Safety Division",
        "sectional_committee": "CHD 8 / MHD (Safety Equipment)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "DPIIT",
        "qco_order_name": "Personal Protective Equipment Quality Mandate",
        "scope": "Specifies minimum requirements for open-circuit compressed air self-contained breathing apparatus (SCBA) used by fire fighters and chemical response teams.",
        "keywords": ["scba", "breathing apparatus", "fire fighting equipment", "compressed air cylinder", "face mask", "toxic gas protection", "respiratory protection"],
        "clauses": [
            {
                "clause_number": "Clause 5.1",
                "clause_title": "Air Delivery Capacity",
                "content": "Apparatus must supply min 300 L/min of air without negative pressure developing inside face piece."
            }
        ]
    },

    # --- PGD (Production & General Engineering Division) ---
    {
        "is_code": "IS 1363 (Part 1):2019",
        "base_code": "IS 1363",
        "part": "Part 1",
        "title": "Hexagon Head Bolts, Screws and Nuts of Product Grade C - Part 1: Hexagon Head Bolts (Size Range M5 to M64)",
        "publication_year": 2019,
        "reaffirmed_year": 2024,
        "edition": "Fifth Revision",
        "division_code": "PGD",
        "division_name": "Production & General Engineering Division",
        "sectional_committee": "PGD 31 (Bolts, Nuts and Fasteners)",
        "status": "ACTIVE",
        "supersedes": ["IS 1363 (Part 1):2002"],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "DPIIT",
        "qco_order_name": "Fasteners (Quality Control) Order, 2023",
        "scope": "Specifies characteristics of hexagon head bolts with metric threads from M5 to M64 of product grade C for general engineering and construction assemblies.",
        "keywords": ["bolts", "hex bolts", "nuts and bolts", "fasteners", "threaded fasteners", "property class 4.6", "m16 bolt", "m20 bolt", "structural fasteners"],
        "clauses": [
            {
                "clause_number": "Clause 4.1",
                "clause_title": "Mechanical Properties",
                "content": "Fasteners shall conform to property classes 4.6, 5.6, or 8.8 as specified in IS 1367 (Part 3)."
            }
        ]
    },
    {
        "is_code": "IS 6438:1980",
        "base_code": "IS 6438",
        "part": null,
        "title": "Aluminium Phosphide Formulations - Specification",
        "publication_year": 1980,
        "reaffirmed_year": 2020,
        "edition": "First Revision",
        "division_code": "PGD",
        "division_name": "Production & Chemical Division (Grain Preservation)",
        "sectional_committee": "FAD 1 / PGD (Pest Management)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "Ministry of Agriculture / Central Insecticides Board",
        "qco_order_name": "Insecticides & Fumigants Mandate",
        "scope": "Prescribes requirements and methods of test for aluminium phosphide tablet and pellet formulations used for grain fumigation in FCI silos and CWC warehouses against pests.",
        "keywords": ["aluminium phosphide", "grain fumigant", "phosphine gas", "godown fumigation", "fci grain preservation", "pest control tablets", "cwc warehouse"],
        "clauses": [
            {
                "clause_number": "Clause 3.1",
                "clause_title": "Phosphine Generation Content",
                "content": "Each 3.0 g tablet shall release not less than 1.0 g of phosphine gas (PH3) upon exposure to atmospheric moisture."
            }
        ]
    },

    # --- WRD (Water Resources Division) ---
    {
        "is_code": "IS 778:1984",
        "base_code": "IS 778",
        "part": null,
        "title": "Copper Alloy Gate, Globe and Check Valves for Water Works Purposes - Specification",
        "publication_year": 1984,
        "reaffirmed_year": 2020,
        "edition": "Fourth Revision",
        "division_code": "WRD",
        "division_name": "Water Resources Division",
        "sectional_committee": "WRD 22 (Valves and Sluices)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "DPIIT",
        "qco_order_name": "Valves Quality Control Order",
        "scope": "Covers copper alloy (bronze and brass) gate valves, globe valves and check valves suitable for water works pipelines with working pressures up to 1.6 MPa.",
        "keywords": ["valves", "gate valve", "check valve", "globe valve", "bronze valve", "water distribution", "irrigation sluice", "plumbing valve"],
        "clauses": [
            {
                "clause_number": "Clause 8.1",
                "clause_title": "Hydraulic Test",
                "content": "Body test pressure shall be 1.5 times the maximum rated working pressure, held for 2 minutes without leakage."
            }
        ]
    },
    {
        "is_code": "IS 2951 (Part 1):1965",
        "base_code": "IS 2951",
        "part": "Part 1",
        "title": "Recommendation for Estimation of Flow of Water in Open Channels - Part 1: Velocity Area Methods",
        "publication_year": 1965,
        "reaffirmed_year": 2021,
        "edition": "First Edition",
        "division_code": "WRD",
        "division_name": "Water Resources Division",
        "sectional_committee": "WRD 1 (Hydrometry)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": false,
        "qco_ministry": null,
        "qco_order_name": null,
        "scope": "Lays down recommendations for estimating flow velocity and discharge of water in rivers, irrigation canals and open channels using current meters and float methods.",
        "keywords": ["flow measurement", "open channel", "canal flow", "water resources", "discharge estimation", "irrigation canal", "current meter"],
        "clauses": [
            {
                "clause_number": "Clause 5.1",
                "clause_title": "Velocity Measurement",
                "content": "Specifies two-point method (0.2 and 0.8 depth) and one-point method (0.6 depth) for determining mean vertical velocity."
            }
        ]
    },

    # --- MSD (Management & Systems Division) ---
    {
        "is_code": "IS/ISO 9001:2015",
        "base_code": "IS/ISO 9001",
        "part": null,
        "title": "Quality Management Systems - Requirements",
        "publication_year": 2015,
        "reaffirmed_year": 2021,
        "edition": "Fifth Edition",
        "division_code": "MSD",
        "division_name": "Management & Systems Division",
        "sectional_committee": "MSD 2 (Quality Management)",
        "status": "ACTIVE",
        "supersedes": ["IS/ISO 9001:2008"],
        "superseded_by": null,
        "mandatory_qco": false,
        "qco_ministry": null,
        "qco_order_name": null,
        "scope": "Specifies requirements for a quality management system (QMS) when an organization needs to demonstrate its ability to consistently provide products and services that meet customer and applicable statutory requirements.",
        "keywords": ["iso 9001", "qms", "quality management", "vendor qualification", "quality audit", "process control", "statutory compliance"],
        "clauses": [
            {
                "clause_number": "Clause 8.4",
                "clause_title": "Control of Externally Provided Processes, Products and Services",
                "content": "The organization shall ensure that externally provided processes, products and services conform to requirements and do not adversely affect quality."
            }
        ]
    },
    {
        "is_code": "IS/ISO 14001:2015",
        "base_code": "IS/ISO 14001",
        "part": null,
        "title": "Environmental Management Systems - Requirements with Guidance for Use",
        "publication_year": 2015,
        "reaffirmed_year": 2021,
        "edition": "Third Edition",
        "division_code": "MSD",
        "division_name": "Management & Systems Division",
        "sectional_committee": "MSD 12 (Environmental Management)",
        "status": "ACTIVE",
        "supersedes": ["IS/ISO 14001:2004"],
        "superseded_by": null,
        "mandatory_qco": false,
        "qco_ministry": null,
        "qco_order_name": null,
        "scope": "Specifies requirements for an environmental management system that an organization can use to enhance its environmental performance, fulfill compliance obligations, and achieve environmental objectives.",
        "keywords": ["iso 14001", "ems", "environmental management", "pollution control", "green procurement", "sustainability"],
        "clauses": [
            {
                "clause_number": "Clause 6.1",
                "clause_title": "Environmental Aspects",
                "content": "Organization shall determine environmental aspects of activities, products and services that it can control."
            }
        ]
    },
    {
        "is_code": "IS/ISO 45001:2018",
        "base_code": "IS/ISO 45001",
        "part": null,
        "title": "Occupational Health and Safety Management Systems - Requirements with Guidance for Use",
        "publication_year": 2018,
        "reaffirmed_year": 2023,
        "edition": "First Edition",
        "division_code": "MSD",
        "division_name": "Management & Systems Division",
        "sectional_committee": "MSD 14 (Occupational Safety and Health)",
        "status": "ACTIVE",
        "supersedes": ["IS 18001:2007"],
        "superseded_by": null,
        "mandatory_qco": false,
        "qco_ministry": null,
        "qco_order_name": null,
        "scope": "Specifies requirements for an occupational health and safety (OH&S) management system to enable organizations to provide safe and healthy workplaces, prevent work-related injury and ill health.",
        "keywords": ["iso 45001", "occupational safety", "worker health", "hazard identification", "safety management"],
        "clauses": [
            {
                "clause_number": "Clause 8.1",
                "clause_title": "Operational Planning and Control",
                "content": "Organization shall establish processes for the elimination of hazards and reduction of OH&S risks."
            }
        ]
    },

    # --- TXD (Textiles Division) ---
    {
        "is_code": "IS 16186:2014",
        "base_code": "IS 16186",
        "part": null,
        "title": "Textiles - Jute Bags for Packing 50 kg Sugar - Specification",
        "publication_year": 2014,
        "reaffirmed_year": 2020,
        "edition": "First Edition",
        "division_code": "TXD",
        "division_name": "Textiles Division (Food Packaging)",
        "sectional_committee": "TXD 3 (Jute Products)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "Ministry of Textiles & DFPD",
        "qco_order_name": "Jute Packaging Materials (Compulsory Use in Packing Commodities) Mandate",
        "scope": "Prescribes constructional details and requirements of lightweight B.Twill jute bags for packing 50 kg sugar produced by sugar mills for central pool and PDS allocation.",
        "keywords": ["sugar bags", "jute sugar bags", "fci sugar", "pds sugar packing", "50 kg sugar sack", "b twill sugar bag"],
        "clauses": [
            {
                "clause_number": "Clause 4.1",
                "clause_title": "Dimensions",
                "content": "Outside length: 910 mm; Outside width: 560 mm; Mass: 580 g."
            }
        ]
    },
    {
        "is_code": "IS 16654:2017",
        "base_code": "IS 16654",
        "part": null,
        "title": "Geosynthetics - Polypropylene Nonwoven Geotextiles for Highways - Specification",
        "publication_year": 2017,
        "reaffirmed_year": 2022,
        "edition": "First Edition",
        "division_code": "TXD",
        "division_name": "Textiles Division (Technical Textiles)",
        "sectional_committee": "TXD 30 (Geosynthetics)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "Ministry of Textiles / MoRTH",
        "qco_order_name": "Technical Textiles Quality Control Order",
        "scope": "Covers mechanical, hydraulic, and endurance requirements of polypropylene nonwoven needle-punched geotextiles used in subgrade separation and stabilization of roads and expressways.",
        "keywords": ["geotextile", "polypropylene geotextile", "road stabilization", "subgrade separation", "drainage fabric", "highway construction", "morth specification"],
        "clauses": [
            {
                "clause_number": "Clause 5.1",
                "clause_title": "Tensile and Puncture Strength",
                "content": "Trapezoidal tear strength min 250 N; CBR puncture resistance min 1500 N; Apparent opening size (AOS) <= 150 microns."
            }
        ]
    },
    {
        "is_code": "IS 745:1990",
        "base_code": "IS 745",
        "part": null,
        "title": "Handloom Cotton Bed Sheets - Specification",
        "publication_year": 1990,
        "reaffirmed_year": 2021,
        "edition": "Second Revision",
        "division_code": "TXD",
        "division_name": "Textiles Division",
        "sectional_committee": "TXD 7 (Handloom and Khadi)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": false,
        "qco_ministry": null,
        "qco_order_name": null,
        "scope": "Prescribes constructional particulars and other performance requirements for grey, scoured, bleached, dyed, striped, checked or printed handloom and powerloom cotton bed sheets used in hospitals and institutions.",
        "keywords": ["cotton bed sheets", "hospital bedsheets", "hospital linen", "bleached cotton", "bedsheets", "cotton sheets", "thread count", "gsm", "breaking strength", "medical textiles", "dghs linen", "patient bedsheets"],
        "clauses": [
            {
                "clause_number": "Clause 4.1",
                "clause_title": "Physical and Dimensional Requirements",
                "content": "Dimensions as specified; Mass per unit area min 140 g/m2; Breaking strength warp min 350 N, weft min 300 N; Thread count min 180 TC."
            },
            {
                "clause_number": "Clause 5.2",
                "clause_title": "Whiteness and Fastness",
                "content": "Whiteness index min 80%; Dimensional shrinkage after wash not exceeding 3.0% warp and 2.0% weft; Colour fastness rating min 4."
            }
        ]
    },

    # --- CHD (Chemical Division) ---
    {
        "is_code": "IS 515:1959",
        "base_code": "IS 515",
        "part": null,
        "title": "Specification for Bleaching Powder, Stable",
        "publication_year": 1959,
        "reaffirmed_year": 2020,
        "edition": "First Revision",
        "division_code": "CHD",
        "division_name": "Chemical Division",
        "sectional_committee": "CHD 1 (Inorganic Chemicals)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": false,
        "qco_ministry": null,
        "qco_order_name": null,
        "scope": "Prescribes requirements and methods of sampling and test for stable bleaching powder (chlorinated lime) for water treatment, public health sanitation and municipal disinfection.",
        "keywords": ["bleaching powder", "chlorinated lime", "water disinfection", "available chlorine", "calcium hypochlorite", "sanitation chemical", "water works chemical"],
        "clauses": [
            {
                "clause_number": "Clause 4.1",
                "clause_title": "Available Chlorine Content",
                "content": "Available chlorine shall be not less than 32.0 percent by mass; Moisture max 0.3%."
            }
        ]
    },
    {
        "is_code": "IS 15477:2019",
        "base_code": "IS 15477",
        "part": null,
        "title": "Adhesives for Use with Ceramic, Mosaic and Stone Tiles - Specification",
        "publication_year": 2019,
        "reaffirmed_year": 2024,
        "edition": "Second Revision",
        "division_code": "CHD",
        "division_name": "Chemical Division",
        "sectional_committee": "CED 30 / CHD (Adhesives)",
        "status": "ACTIVE",
        "supersedes": ["IS 15477:2004"],
        "superseded_by": null,
        "mandatory_qco": false,
        "qco_ministry": null,
        "qco_order_name": null,
        "scope": "Specifies chemical and physical requirements for polymer-modified cementitious adhesives used for fixing ceramic, vitrified and natural stone tiles.",
        "keywords": ["tile adhesive", "ceramic adhesive", "polymer modified adhesive", "vitrified tile fixing", "tensile adhesion strength", "shear adhesion"],
        "clauses": [
            {
                "clause_number": "Clause 4.1",
                "clause_title": "Types of Adhesives",
                "content": "Classified into Type 1 (standard tile adhesive), Type 2 (for heavy vitreous tiles), Type 3 (for external facade), and Type 4 (for dry wall installation)."
            }
        ]
    },
    {
        "is_code": "IS 1893 (Part 1):2016",
        "base_code": "IS 1893",
        "part": "Part 1",
        "title": "Criteria for Earthquake Resistant Design of Structures - Part 1: General Provisions and Buildings",
        "publication_year": 2016,
        "reaffirmed_year": 2021,
        "edition": "Sixth Revision",
        "division_code": "CED",
        "division_name": "Civil Engineering Division",
        "sectional_committee": "CED 39 (Earthquake Engineering)",
        "status": "ACTIVE",
        "supersedes": ["IS 1893:2002"],
        "superseded_by": null,
        "mandatory_qco": false,
        "qco_ministry": null,
        "qco_order_name": null,
        "scope": "Provides criteria for calculating design seismic forces for buildings and structures located in Seismic Zones II, III, IV, and V across India.",
        "keywords": ["earthquake design", "seismic zone", "zone iv", "zone v", "base shear", "response reduction factor", "importance factor", "spectral acceleration"],
        "clauses": [
            {
                "clause_number": "Clause 6.4",
                "clause_title": "Design Horizontal Seismic Coefficient",
                "content": "Calculates horizontal design seismic coefficient Ah using zone factor Z, importance factor I, and response reduction factor R."
            }
        ]
    },
    {
        "is_code": "IS 13920:2016",
        "base_code": "IS 13920",
        "part": null,
        "title": "Ductile Design and Detailing of Reinforced Concrete Structures Subjected to Seismic Forces - Code of Practice",
        "publication_year": 2016,
        "reaffirmed_year": 2021,
        "edition": "First Revision",
        "division_code": "CED",
        "division_name": "Civil Engineering Division",
        "sectional_committee": "CED 39 (Earthquake Engineering)",
        "status": "ACTIVE",
        "supersedes": ["IS 13920:1993"],
        "superseded_by": null,
        "mandatory_qco": false,
        "qco_ministry": null,
        "qco_order_name": null,
        "scope": "Covers requirements for designing and detailing of members of reinforced concrete structures required to resist earthquake effects through high ductility.",
        "keywords": ["ductile detailing", "seismic detailing", "stirrup spacing", "beam column joint", "confining reinforcement", "earthquake resistance"],
        "clauses": [
            {
                "clause_number": "Clause 6.2",
                "clause_title": "Longitudinal Reinforcement in Beams",
                "content": "Minimum longitudinal steel ratio shall be not less than 0.24 sqrt(fck)/fy; both top and bottom bars shall extend into column."
            }
        ]
    },
    {
        "is_code": "IS 2185 (Part 1):2005",
        "base_code": "IS 2185",
        "part": "Part 1",
        "title": "Concrete Masonry Units - Specification - Part 1: Hollow and Solid Concrete Blocks",
        "publication_year": 2005,
        "reaffirmed_year": 2020,
        "edition": "Third Revision",
        "division_code": "CED",
        "division_name": "Civil Engineering Division",
        "sectional_committee": "CED 30 (Clay and Ceramic Products)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": false,
        "qco_ministry": null,
        "qco_order_name": null,
        "scope": "Covers solid and hollow precast concrete blocks for use in load bearing and non-load bearing masonry construction.",
        "keywords": ["concrete blocks", "hollow blocks", "solid concrete blocks", "masonry units", "compressive strength", "drying shrinkage", "moisture movement"],
        "clauses": [
            {
                "clause_number": "Table 1",
                "clause_title": "Compressive Strength of Concrete Blocks",
                "content": "Specifies minimum average compressive strength of hollow blocks from 3.5 MPa to 15.0 MPa based on grade."
            }
        ]
    },
    {
        "is_code": "IS 1200 (Part 1):1992",
        "base_code": "IS 1200",
        "part": "Part 1",
        "title": "Methods of Measurement of Building and Civil Engineering Works - Part 1: Earthwork",
        "publication_year": 1992,
        "reaffirmed_year": 2022,
        "edition": "Fourth Revision",
        "division_code": "CED",
        "division_name": "Civil Engineering Division",
        "sectional_committee": "CED 44 (Method of Measurement)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": false,
        "qco_ministry": null,
        "qco_order_name": null,
        "scope": "Prescribes standard methods of measurement for earthwork excavation, trenching, backfilling and leveling in civil engineering contracts and tenders.",
        "keywords": ["earthwork measurement", "excavation", "trenching", "civil engineering measurement", "boq measurement", "cpwd measurement"],
        "clauses": [
            {
                "clause_number": "Clause 4.1",
                "clause_title": "Classification of Soils",
                "content": "Classifies soils for excavation payment into Ordinary Soil, Hard Soil, Soft Rock, and Hard Rock requiring blasting."
            }
        ]
    },
    {
        "is_code": "IS 3043:2018",
        "base_code": "IS 3043",
        "part": null,
        "title": "Code of Practice for Earthing",
        "publication_year": 2018,
        "reaffirmed_year": 2023,
        "edition": "Second Revision",
        "division_code": "ETD",
        "division_name": "Electrotechnical Division",
        "sectional_committee": "ETD 20 (Electrical Installation)",
        "status": "ACTIVE",
        "supersedes": ["IS 3043:1987"],
        "superseded_by": null,
        "mandatory_qco": false,
        "qco_ministry": null,
        "qco_order_name": null,
        "scope": "Applies to electrical installation earthing systems for power generation, transmission, industrial plants, commercial and domestic buildings to ensure safety against electric shock and equipment damage.",
        "keywords": ["earthing", "grounding", "earth electrode", "plate earthing", "pipe earthing", "earth pit", "soil resistivity", "copper electrode", "substation earthing"],
        "clauses": [
            {
                "clause_number": "Clause 9.1",
                "clause_title": "Earth Electrode Types",
                "content": "Specifies design of rod electrodes, pipe electrodes (min 38mm dia GI pipe), and plate electrodes (600x600mm copper or GI plate) embedded in soil with bentonite or charcoal/salt backfill."
            }
        ]
    },
    {
        "is_code": "IS 2026 (Part 1):2011",
        "base_code": "IS 2026",
        "part": "Part 1",
        "title": "Power Transformers - Part 1: General",
        "publication_year": 2011,
        "reaffirmed_year": 2021,
        "edition": "Second Revision",
        "division_code": "ETD",
        "division_name": "Electrotechnical Division",
        "sectional_committee": "ETD 16 (Transformers)",
        "status": "ACTIVE",
        "supersedes": ["IS 2026 (Part 1):1977"],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "Ministry of Power / DPIIT",
        "qco_order_name": "Power Transformers Quality Mandate",
        "scope": "Specifies requirements for three-phase and single-phase power transformers (including auto-transformers) used in transmission and industrial power grids.",
        "keywords": ["power transformer", "high voltage transformer", "substation transformer", "66 kv", "132 kv", "oil temperature rise", "winding resistance", "impedance voltage"],
        "clauses": [
            {
                "clause_number": "Clause 4.1",
                "clause_title": "Rating and Cooling",
                "content": "Specifies ONAN, ONAF, and OFAF cooling methods and temperature rise limits for oil and windings."
            }
        ]
    },
    {
        "is_code": "IS 12640 (Part 1):2016",
        "base_code": "IS 12640",
        "part": "Part 1",
        "title": "Residual Current Operated Circuit-Breakers (RCCBs) - Part 1: Without Integral Overcurrent Protection for Household Installations",
        "publication_year": 2016,
        "reaffirmed_year": 2021,
        "edition": "Second Revision",
        "division_code": "ETD",
        "division_name": "Electrotechnical Division",
        "sectional_committee": "ETD 14 (Electrical Accessories)",
        "status": "ACTIVE",
        "supersedes": ["IS 12640 (Part 1):2000"],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "DPIIT",
        "qco_order_name": "Circuit Breakers Quality Control Order",
        "scope": "Applies to residual current operated circuit-breakers (RCCB / ELCB) for protecting human life against electrocution and electrical fire hazards.",
        "keywords": ["rccb", "elcb", "residual current breaker", "earth leakage circuit breaker", "30ma rccb", "100ma rccb", "human shock protection", "electrical safety"],
        "clauses": [
            {
                "clause_number": "Clause 5.3",
                "clause_title": "Rated Residual Operating Current",
                "content": "Standard rated residual operating currents (I Delta n) are 10 mA, 30 mA, 100 mA, 300 mA, and 500 mA. 30 mA mandated for direct human contact protection."
            }
        ]
    },
    {
        "is_code": "IS 12615:2018",
        "base_code": "IS 12615",
        "part": null,
        "title": "Line Operated Three-Phase A.C. Motors (IE Code) - Energy Efficient Motors - Specification",
        "publication_year": 2018,
        "reaffirmed_year": 2023,
        "edition": "Third Revision",
        "division_code": "ETD",
        "division_name": "Electrotechnical Division",
        "sectional_committee": "ETD 15 (Rotating Machinery)",
        "status": "ACTIVE",
        "supersedes": ["IS 12615:2011"],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "DPIIT",
        "qco_order_name": "Electric Motors (Quality Control) Order",
        "scope": "Specifies energy efficiency classes (IE2, IE3, and IE4) for three-phase squirrel cage induction motors from 0.12 kW up to 1000 kW operating at 50 Hz.",
        "keywords": ["electric motor", "induction motor", "ie2 motor", "ie3 motor", "energy efficient motor", "three phase motor", "bee motor star rating"],
        "clauses": [
            {
                "clause_number": "Table 1",
                "clause_title": "Nominal Efficiency Limits",
                "content": "Defines strict minimum percentage full-load efficiency across 2-pole, 4-pole, 6-pole and 8-pole ratings for IE2 and premium IE3 classes."
            }
        ]
    },
    {
        "is_code": "IS 616:2017",
        "base_code": "IS 616",
        "part": null,
        "title": "Audio, Video and Similar Electronic Apparatus - Safety Requirements",
        "publication_year": 2017,
        "reaffirmed_year": 2022,
        "edition": "Fourth Edition",
        "division_code": "LITD",
        "division_name": "Electronics & IT Division",
        "sectional_committee": "LITD 7 (Audio, Video and Multimedia Systems)",
        "status": "ACTIVE",
        "supersedes": ["IS 616:2010"],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "MeitY",
        "qco_order_name": "Electronics & IT Goods Compulsory Registration Order",
        "scope": "Applies to electronic apparatus designed to be fed from mains, supplying power, or battery for reception, generation, recording or reproduction of audio and video.",
        "keywords": ["audio video safety", "television", "display monitor", "sound system", "meity crs", "amplifier", "electronic equipment safety"],
        "clauses": [
            {
                "clause_number": "Clause 4.1",
                "clause_title": "General Test Conditions",
                "content": "Apparatus must operate without hazard under normal operation and under single fault condition."
            }
        ]
    },
    {
        "is_code": "IS 814:2004",
        "base_code": "IS 814",
        "part": null,
        "title": "Covered Electrodes for Manual Metal Arc Welding of Carbon and Carbon Manganese Steel - Specification",
        "publication_year": 2004,
        "reaffirmed_year": 2019,
        "edition": "Sixth Revision",
        "division_code": "MTD",
        "division_name": "Metallurgical Engineering Division",
        "sectional_committee": "MTD 11 (Welding)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "Ministry of Steel",
        "qco_order_name": "Welding Consumables Quality Control Order",
        "scope": "Specifies requirements for covered electrodes for manual metal arc welding of mild, normal and medium tensile structural steels.",
        "keywords": ["welding electrodes", "arc welding", "welding rod", "e6013", "e7018", "weld metal tensile strength", "charpy v notch", "structural welding"],
        "clauses": [
            {
                "clause_number": "Clause 5.1",
                "clause_title": "Electrode Classification",
                "content": "Classified by 6-letter designation representing tensile strength, yield stress, elongation, impact values, flux coating and welding position."
            }
        ]
    },
    {
        "is_code": "IS 2830:2012",
        "base_code": "IS 2830",
        "part": null,
        "title": "Carbon Steel Cast Billet Ingots, Billets, Blooms and Slabs for Re-Rolling into Steel for General Structural Purposes - Specification",
        "publication_year": 2012,
        "reaffirmed_year": 2022,
        "edition": "Fourth Revision",
        "division_code": "MTD",
        "division_name": "Metallurgical Engineering Division",
        "sectional_committee": "MTD 4 (Wrought Steel)",
        "status": "ACTIVE",
        "supersedes": ["IS 2830:1992"],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "Ministry of Steel",
        "qco_order_name": "Steel and Steel Products QCO",
        "scope": "Covers chemical and physical requirements of continuously cast carbon steel billets, blooms and slabs used for re-rolling into TMT bars and structural sections.",
        "keywords": ["steel billets", "cast billets", "re-rolling billets", "continuous casting", "carbon steel bloom", "steel slab", "primary steel producer"],
        "clauses": [
            {
                "clause_number": "Clause 6.1",
                "clause_title": "Chemical Composition",
                "content": "Specifies strict maximum limits for Carbon, Manganese, Phosphorus (max 0.050%) and Sulphur (max 0.050%)."
            }
        ]
    },
    {
        "is_code": "IS 10001:1981",
        "base_code": "IS 10001",
        "part": null,
        "title": "Specification for Performance Requirements for Constant Speed Compression Ignition (Diesel) Engines for Agricultural and Industrial Use",
        "publication_year": 1981,
        "reaffirmed_year": 2020,
        "edition": "First Edition",
        "division_code": "MED",
        "division_name": "Mechanical Engineering Division",
        "sectional_committee": "MED 3 (Internal Combustion Engines)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "DPIIT",
        "qco_order_name": "Diesel Engines Quality Mandate",
        "scope": "Specifies performance, fuel consumption, governor characteristics and testing requirements for single cylinder constant speed diesel engines up to 20 kW.",
        "keywords": ["diesel engine", "agricultural engine", "constant speed engine", "irrigation diesel engine", "specific fuel consumption", "governor test"],
        "clauses": [
            {
                "clause_number": "Clause 6.1",
                "clause_title": "Specific Fuel Consumption",
                "content": "Specific fuel consumption at rated continuous output shall not exceed manufacturer guaranteed value by more than 5%."
            }
        ]
    },
    {
        "is_code": "IS 8148:2003",
        "base_code": "IS 8148",
        "part": null,
        "title": "Packaged Air Conditioners - Specification",
        "publication_year": 2003,
        "reaffirmed_year": 2019,
        "edition": "First Revision",
        "division_code": "MED",
        "division_name": "Mechanical Engineering Division",
        "sectional_committee": "MED 3 (Air Conditioning and Refrigeration)",
        "status": "ACTIVE",
        "supersedes": ["IS 8148:1976"],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "DPIIT",
        "qco_order_name": "Air Conditioners Quality Control Order",
        "scope": "Prescribes constructional and performance requirements for factory-assembled packaged air conditioners with water-cooled or air-cooled condensers.",
        "keywords": ["packaged air conditioner", "central ac", "ductable ac", "cooling capacity", "cop", "refrigerant", "commercial air conditioning"],
        "clauses": [
            {
                "clause_number": "Clause 8.1",
                "clause_title": "Cooling Capacity Test",
                "content": "Total cooling capacity shall not be less than 95% of rated capacity at standard rating conditions."
            }
        ]
    },
    {
        "is_code": "IS 13428:2005",
        "base_code": "IS 13428",
        "part": null,
        "title": "Packaged Natural Mineral Water - Specification",
        "publication_year": 2005,
        "reaffirmed_year": 2021,
        "edition": "Second Revision",
        "division_code": "FAD",
        "division_name": "Food and Agriculture Division",
        "sectional_committee": "FAD 14 (Drinks and Drinking Water)",
        "status": "ACTIVE",
        "supersedes": ["IS 13428:1998"],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "Ministry of Consumer Affairs / FSSAI",
        "qco_order_name": "Natural Mineral Water Compulsory Certification Order",
        "scope": "Prescribes requirements and methods of test for packaged natural mineral water obtained directly from natural subterranean or spring sources.",
        "keywords": ["mineral water", "natural mineral water", "spring water", "packaged water", "compulsory isi mark", "tds minerals", "potable water"],
        "clauses": [
            {
                "clause_number": "Table 1",
                "clause_title": "Physico-Chemical Characteristics",
                "content": "Total dissolved solids between 150 mg/L and 700 mg/L naturally derived without demineralization."
            }
        ]
    },
    {
        "is_code": "IS 4151:2015",
        "base_code": "IS 4151",
        "part": null,
        "title": "Protective Helmets for Two-Wheeler Riders - Specification",
        "publication_year": 2015,
        "reaffirmed_year": 2020,
        "edition": "Fourth Revision",
        "division_code": "TED",
        "division_name": "Transport Engineering Division",
        "sectional_committee": "TED 28 (Safety Equipment)",
        "status": "ACTIVE",
        "supersedes": ["IS 4151:1993"],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "Ministry of Road Transport and Highways (MoRTH)",
        "qco_order_name": "Two-Wheeler Helmets (Quality Control) Order",
        "scope": "Specifies requirements regarding construction, materials, shock absorption, retention system, and penetration resistance for two-wheeler protective helmets.",
        "keywords": ["helmet", "motorcycle helmet", "two wheeler helmet", "rider helmet", "isi helmet", "shock absorption", "chin strap retention", "visor light transmission"],
        "clauses": [
            {
                "clause_number": "Clause 6.1",
                "clause_title": "Impact Shock Absorption",
                "content": "Peak acceleration imparted to headform shall not exceed 300 g at any impact test site."
            }
        ]
    },
    {
        "is_code": "IS 3237 (Part 1):1985",
        "base_code": "IS 3237",
        "part": "Part 1",
        "title": "Hypodermic Syringes for Single Use - Part 1: Sterile Medical Syringes",
        "publication_year": 1985,
        "reaffirmed_year": 2021,
        "edition": "Second Revision",
        "division_code": "MHD",
        "division_name": "Medical Equipment & Hospital Planning Division",
        "sectional_committee": "MHD 12 (Hospital Supplies)",
        "status": "ACTIVE",
        "supersedes": [],
        "superseded_by": null,
        "mandatory_qco": true,
        "qco_ministry": "CDSCO / Ministry of Health",
        "qco_order_name": "Sterile Medical Devices Quality Mandate",
        "scope": "Prescribes requirements for sterile single-use hypodermic syringes made of plastic or glass for aspiration and injection of fluids.",
        "keywords": ["disposable syringe", "hypodermic syringe", "sterile syringe", "medical supplies", "hospital tender", "luer taper", "plunger leak test"],
        "clauses": [
            {
                "clause_number": "Clause 4.1",
                "clause_title": "Liquid and Air Leakage Test",
                "content": "No leakage past piston and seal shall occur under 300 kPa internal hydrostatic pressure."
            }
        ]
    }
]

# Merge and deduplicate
final_standards = list(existing_standards)
added_count = 0
for std in new_standards:
    if std["base_code"] not in existing_codes:
        final_standards.append(std)
        existing_codes.add(std["base_code"])
        added_count += 1

# Save back to file
with open(CATALOG_PATH, "w", encoding="utf-8") as f:
    json.dump(final_standards, f, indent=2)

print(f"Successfully added {added_count} new standards.")
print(f"Total standards now in catalog: {len(final_standards)}")

# Verify 14 divisions
divisions = set(s["division_code"] for s in final_standards)
print(f"Total Division Councils represented ({len(divisions)}): {sorted(list(divisions))}")
