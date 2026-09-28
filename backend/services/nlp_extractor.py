import re
import json
from typing import List, Dict, Any, Optional
from backend.config import BRANDS_GAZETTEER_PATH
from backend.models.schemas import ExtractedParameters, PhysicalDimension

class NLPExtractor:
    def __init__(self):
        self.brands_list = self._load_brands()

    def _load_brands(self) -> List[Dict[str, str]]:
        if BRANDS_GAZETTEER_PATH.exists():
            try:
                with open(BRANDS_GAZETTEER_PATH, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("brands", [])
            except Exception:
                return []
        return []

    def extract_parameters(self, text: str) -> ExtractedParameters:
        """Extract structured technical parameters from unstructured specification text."""
        
        # 1. Detect Cited Standard Patterns (e.g., IS 1786, IS 1139, IS:456, IS 1239 Pt 1)
        cited_standards = self._extract_cited_standards(text)
        
        # 2. Detect Brands
        detected_brands = self._detect_brands(text)
        
        # 3. Detect Commodity Name
        commodity_name = self._extract_commodity(text)
        
        # 4. Material Grades
        material_grade = self._extract_material_grade(text)
        
        # 5. Physical Dimensions
        physical_dimensions = self._extract_dimensions(text)
        
        # 6. Electrical Ratings
        electrical_ratings = self._extract_electrical_ratings(text)
        
        # 7. Mechanical Ratings
        mechanical_ratings = self._extract_mechanical_ratings(text)
        
        # 8. Testing Requirements
        testing_requirements = self._extract_testing_requirements(text)
        
        # 9. Intended Application
        intended_app = self._extract_application(text)

        return ExtractedParameters(
            commodity_name=commodity_name,
            material_grade=material_grade,
            intended_application=intended_app,
            physical_dimensions=physical_dimensions,
            electrical_ratings=electrical_ratings,
            mechanical_ratings=mechanical_ratings,
            testing_requirements=testing_requirements,
            detected_standard_citations=cited_standards,
            detected_brands=detected_brands
        )

    def _extract_cited_standards(self, text: str) -> List[str]:
        # Matches IS 1786, IS 1139:1966, IS:456-2000, IS 1239 (Part 1):2004, etc.
        pattern = re.compile(
            r'\bIS\s*(?:[:\s-]?\s*)(\d{3,5})(?:\s*(?:\(|Part|Pt)[\s\.]*(\d+)\)?)?(?:\s*[:\s-]?\s*(\d{4}))?\b',
            re.IGNORECASE
        )
        matches = pattern.finditer(text)
        found = []
        for m in matches:
            is_num = m.group(1)
            part = m.group(2)
            year = m.group(3)
            formatted = f"IS {is_num}"
            if part:
                formatted += f" (Part {part})"
            if year:
                formatted += f":{year}"
            if formatted not in found:
                found.append(formatted)
        return found

    def _detect_brands(self, text: str) -> List[str]:
        found_brands = []
        lower_text = text.lower()
        for b in self.brands_list:
            b_name = b["name"]
            # Look for whole word brand name
            pattern = r'\b' + re.escape(b_name.lower()) + r'\b'
            if re.search(pattern, lower_text):
                if b_name not in found_brands:
                    found_brands.append(b_name)
        return found_brands

    def _extract_commodity(self, text: str) -> str:
        # Common commodity patterns in public procurement
        commodities = [
            ("fortified rice kernel", "Fortified Rice Kernels (FRK)"),
            ("fortified rice", "Fortified Rice Kernels (FRK)"),
            ("frk", "Fortified Rice Kernels (FRK)"),
            ("wheat atta", "Wheat Atta (Whole Meal)"),
            ("wheat flour", "Wheat Atta (Flour)"),
            ("atta", "Wheat Atta"),
            ("iodized salt", "Iodized Salt (Vacuum Evaporated)"),
            ("table salt", "Iodized Salt"),
            ("jute bag", "Jute Bags for Packing 50 kg Foodgrains"),
            ("b twill", "B.Twill Jute Bags for Foodgrains"),
            ("gunny bag", "Jute Bags for Packing Foodgrains"),
            ("tmt steel rebar", "TMT Steel Reinforcement Bars"),
            ("deformed steel bar", "High Strength Deformed Steel Reinforcement Bars"),
            ("steel rebar", "Steel Reinforcement Bars"),
            ("reinforcement bar", "Steel Reinforcement Bars"),
            ("pvc insulated cable", "PVC Insulated Electric Cables"),
            ("flexible cable", "PVC Insulated Flexible Cable"),
            ("power cable", "Electric Power Cable"),
            ("control cable", "Electric Control Cable"),
            ("wire", "Electric Wire / Cable"),
            ("centrifugal pump", "Horizontal Centrifugal Water Pump"),
            ("water pump", "Centrifugal Water Pump"),
            ("safety helmet", "Industrial Safety Helmet"),
            ("hard hat", "Industrial Safety Helmet"),
            ("filtering half mask", "Respiratory Protective Filtering Half Mask"),
            ("n95 mask", "Respiratory Protective Particulate Respirator"),
            ("respirator", "Respiratory Protective Device"),
            ("portland pozzolana cement", "Portland Pozzolana Cement (PPC)"),
            ("ppc cement", "Portland Pozzolana Cement (PPC)"),
            ("ordinary portland cement", "Ordinary Portland Cement (OPC)"),
            ("opc cement", "Ordinary Portland Cement (OPC)"),
            ("cement", "Hydraulic Cement"),
            ("steel tube", "Mild Steel Tubes / Pipes"),
            ("steel pipe", "Mild Steel Pipes"),
            ("gi pipe", "Galvanized Mild Steel Pipe"),
            ("structural steel", "Hot Rolled Structural Steel"),
            ("packaged drinking water", "Packaged Drinking Water"),
            ("disinfectant fluid", "Phenolic Disinfectant Fluid"),
            ("liquid hand wash", "Liquid Hand Wash Sanitizer"),
            ("clay brick", "Burnt Clay Building Bricks"),
            ("plug", "Plugs and Socket-Outlets"),
            ("socket", "Plugs and Socket-Outlets"),
            ("laptop", "Portable Laptop Computer"),
            ("desktop", "Desktop Personal Computer")
        ]
        
        lower = text.lower()
        for pattern_str, standard_name in commodities:
            if pattern_str in lower:
                return standard_name

        # Fallback heuristic: Extract first capitalized phrase or line
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        for l in lines:
            if any(k in l.lower() for k in ["supply of", "procurement of", "item:", "item description"]):
                clean = re.sub(r'^(?:supply of|procurement of|item:?|item description:?)\s*', '', l, flags=re.IGNORECASE).strip()
                return clean[:60]
                
        return "General Procurement Commodity"

    def _extract_material_grade(self, text: str) -> Optional[str]:
        # Matches Fe 500D, Fe 415, Fe 550, Grade 43, Grade 53, Grade FG 200, E250, Type A, Class 5, SS 316
        patterns = [
            r'\b(Fe\s*(?:415D?|500D?|550D?|600))\b',
            r'\b((?:33|43|53)\s*Grade)\b',
            r'\b(Grade\s*(?:33|43|53|FG\s*200|LTB\s*2))\b',
            r'\b(E\s*(?:250|275|300|350|410|450))\b',
            r'\b(Type\s*[A-D])\b',
            r'\b(Class\s*[A-C1-5])\b',
            r'\b(SS\s*(?:304|316L?))\b',
            r'\b(HDPE|Polyethylene|PVC|Plain Copper|Electrolytic Copper)\b'
        ]
        found = []
        for p in patterns:
            matches = re.finditer(p, text, re.IGNORECASE)
            for m in matches:
                val = m.group(1).strip()
                if val.upper() not in [x.upper() for x in found]:
                    found.append(val)
        return ", ".join(found) if found else None

    def _extract_dimensions(self, text: str) -> List[PhysicalDimension]:
        dimensions = []
        
        # Diameter patterns: e.g. 12 mm, 16 mm, 20mm diameter, sizes: 4mm to 40mm
        dia_match = re.findall(r'(\d+(?:\.\d+)?)\s*(?:mm|millimeter)s?\s*(?:dia|diameter|size)?', text, re.IGNORECASE)
        if dia_match:
            unique_dias = list(dict.fromkeys(dia_match))[:5]
            dimensions.append(PhysicalDimension(
                parameter_name="Nominal Diameters / Sizes",
                value=f"{', '.join(unique_dias)} mm",
                tolerance=None
            ))
            
        # Length pattern: e.g., 12 meter, 100 meters
        length_match = re.search(r'(\d+(?:\.\d+)?)\s*(?:meter|metre|m)s?\s*(?:length)?', text, re.IGNORECASE)
        if length_match:
            dimensions.append(PhysicalDimension(
                parameter_name="Length",
                value=f"{length_match.group(1)} meters"
            ))

        # Mass tolerance: e.g. +/- 7%, +- 5 percent
        tol_match = re.search(r'(\+\/?-\s*\d+(?:\.\d+)?\s*%)', text)
        if tol_match and dimensions:
            dimensions[0].tolerance = tol_match.group(1).strip()

        return dimensions

    def _extract_electrical_ratings(self, text: str) -> List[str]:
        ratings = []
        
        # Voltage: e.g. 1100 V, 415 Volts AC, 250V, 3 kV
        v_matches = re.findall(r'(\d+(?:\.\d+)?\s*(?:kV|k\.V\.|V|Volts?)\s*(?:AC|DC)?)', text, re.IGNORECASE)
        for v in v_matches:
            v_clean = v.strip()
            if v_clean not in ratings:
                ratings.append(v_clean)
                
        # Current: e.g. 6 A, 16 A, 100 Amps
        i_matches = re.findall(r'(\d+(?:\.\d+)?\s*(?:A|Amps?|Amperes?))\b', text, re.IGNORECASE)
        for i in i_matches:
            i_clean = i.strip()
            if i_clean not in ratings:
                ratings.append(i_clean)

        # Frequency: 50 Hz
        if re.search(r'\b50\s*Hz\b', text, re.IGNORECASE):
            ratings.append("50 Hz")

        return ratings

    def _extract_mechanical_ratings(self, text: str) -> List[str]:
        ratings = []
        
        # Yield stress / proof stress: e.g. 500 MPa, 500 N/mm2
        stress_match = re.search(r'(?:yield\s*stress|proof\s*stress|tensile\s*strength)[^\d]*(\d+(?:\.\d+)?\s*(?:MPa|N\/mm2))', text, re.IGNORECASE)
        if stress_match:
            ratings.append(f"Yield/Proof Stress: {stress_match.group(1)}")
            
        # Elongation: e.g. 16% elongation
        elong_match = re.search(r'(\d+(?:\.\d+)?\s*%)\s*(?:elongation)?', text, re.IGNORECASE)
        if elong_match and "elongation" in text.lower():
            ratings.append(f"Elongation: {elong_match.group(1)}")

        # Pressure / Head: e.g. 10 bar, 5 MPa, 50 meters head
        press_match = re.search(r'(\d+(?:\.\d+)?\s*(?:bar|MPa|kg\/cm2|meters?\s*head))', text, re.IGNORECASE)
        if press_match:
            ratings.append(f"Operating/Test Pressure: {press_match.group(1)}")

        # Force: 5.0 kN
        force_match = re.search(r'(\d+(?:\.\d+)?\s*kN)', text, re.IGNORECASE)
        if force_match:
            ratings.append(f"Impact Force Rating: {force_match.group(1)}")

        # Food & Grain Parameters: Moisture
        moist_match = re.search(r'moisture[^\d]*(\d+(?:\.\d+)?\s*%)', text, re.IGNORECASE)
        if moist_match:
            ratings.append(f"Max Moisture Content: {moist_match.group(1)}")

        # Food & Grain Parameters: Micronutrients (FRK)
        iron_match = re.search(r'iron[^\d]*(\d+(?:\s*to\s*\d+)?\s*mg)', text, re.IGNORECASE)
        if iron_match:
            ratings.append(f"Iron Fortification: {iron_match.group(1)} / 100g")

        folic_match = re.search(r'folic\s*acid[^\d]*(\d+(?:\s*to\s*\d+)?\s*(?:mcg|micrograms?))', text, re.IGNORECASE)
        if folic_match:
            ratings.append(f"Folic Acid: {folic_match.group(1)} / 100g")

        # Gluten (Atta)
        gluten_match = re.search(r'gluten[^\d]*(\d+(?:\.\d+)?\s*%)', text, re.IGNORECASE)
        if gluten_match:
            ratings.append(f"Min Gluten (dry basis): {gluten_match.group(1)}")

        return ratings

    def _extract_testing_requirements(self, text: str) -> List[str]:
        tests = []
        test_keywords = [
            ("bend and rebend", "Bend and Rebend Test"),
            ("hydrostatic", "Hydrostatic Pressure Test"),
            ("shock absorption", "Shock Absorption Test"),
            ("penetration resistance", "Penetration Resistance Test"),
            ("spark test", "Spark Test"),
            ("flame retardant", "Flame Retardance & Oxygen Index Test"),
            ("voltage test in water", "High Voltage Immersion Test in Water"),
            ("compressive strength", "Compressive Strength Test (at specified intervals)"),
            ("chemical composition", "Chemical Composition Spectrometry Analysis"),
            ("insulation resistance", "Insulation Resistance Test"),
            ("hydrocarbon", "Freedom from Hydrocarbons Batching Oil Test"),
            ("extrusion", "Extrusion Density & Water Resistance Test")
        ]
        lower = text.lower()
        for kw, full_test in test_keywords:
            if kw in lower:
                tests.append(full_test)
        return tests

    def _extract_application(self, text: str) -> Optional[str]:
        # Contextual clue extraction
        app_patterns = [
            r'for\s+([A-Za-z0-9\s,\-]{5,50}?)(?:\.|\n|;)',
            r'application:?\s*([^\n\.]+)',
            r'intended\s+use:?\s*([^\n\.]+)'
        ]
        for p in app_patterns:
            m = re.search(p, text, re.IGNORECASE)
            if m:
                cand = m.group(1).strip()
                if len(cand) > 5 and not any(x in cand.lower() for x in ["supply of", "tender", "contract"]):
                    return cand[:80]
        return None
