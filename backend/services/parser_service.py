import re
from typing import Optional, Tuple
import pymupdf

class ParserService:
    @staticmethod
    def extract_text_from_bytes(file_bytes: bytes, filename: str) -> str:
        """Extract clean text from PDF, DOCX, or TXT file bytes."""
        extension = filename.lower().split(".")[-1]
        
        if extension == "pdf":
            return ParserService._extract_from_pdf(file_bytes)
        elif extension == "docx":
            return ParserService._extract_from_docx(file_bytes)
        elif extension in ["txt", "text", "csv"]:
            return file_bytes.decode("utf-8", errors="ignore")
        else:
            # Fallback attempt decoding as text
            return file_bytes.decode("utf-8", errors="ignore")

    @staticmethod
    def _extract_from_pdf(pdf_bytes: bytes) -> str:
        text_parts = []
        try:
            doc = pymupdf.open(stream=pdf_bytes, filetype="pdf")
            for page in doc:
                text = page.get_text("text")
                if text:
                    text_parts.append(text)
            doc.close()
        except Exception as e:
            text_parts.append(f"Error parsing PDF: {str(e)}")
        
        return "\n".join(text_parts)

    @staticmethod
    def _extract_from_docx(docx_bytes: bytes) -> str:
        try:
            import io
            import docx
            doc = docx.Document(io.BytesIO(docx_bytes))
            return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
        except Exception as e:
            return f"Error parsing DOCX: {str(e)}"

    @staticmethod
    def isolate_technical_sections(raw_text: str) -> Tuple[str, Optional[str]]:
        """
        Filters out generic contractual boilerplate and isolates technical specifications.
        Returns: (isolated_technical_text, detected_tender_reference)
        """
        lines = raw_text.splitlines()
        
        # Regex for tender references (e.g. NIT No. 123/2026, GEM/2026/B/1234)
        tender_ref_match = re.search(
            r'(?:NIT\s*(?:No\.?|Number)|Tender\s*No\.?|Bid\s*No\.?|GeM\s*Bid\s*No\.?)[\s:]*([A-Za-z0-9\/\-_]+)',
            raw_text,
            re.IGNORECASE
        )
        tender_reference = tender_ref_match.group(1).strip() if tender_ref_match else None

        # Headers signaling technical specification sections
        tech_header_pattern = re.compile(
            r'^(?:schedule\s+of\s+requirements|technical\s+specifications?|specification\s+schedule|item\s+description|scope\s+of\s+supply|technical\s+parameters?)\b',
            re.IGNORECASE
        )

        # Boilerplate sections to skip if detected later
        boilerplate_header_pattern = re.compile(
            r'^(?:general\s+conditions\s+of\s+contract|instructions\s+to\s+bidders|arbitration|liquidated\s+damages|earnest\s+money\s+deposit|emd|payment\s+terms)\b',
            re.IGNORECASE
        )

        captured_lines = []
        is_capturing = False
        saw_explicit_header = False

        for line in lines:
            trimmed = line.strip()
            if not trimmed:
                continue

            if tech_header_pattern.search(trimmed):
                is_capturing = True
                saw_explicit_header = True
                captured_lines.append(trimmed)
                continue

            if boilerplate_header_pattern.search(trimmed) and is_capturing and len(captured_lines) > 5:
                # Stop capturing once boilerplate starts
                is_capturing = False
                continue

            if is_capturing:
                captured_lines.append(trimmed)

        # If no explicit technical section headers found, use the cleaned raw text
        if not saw_explicit_header or len(captured_lines) < 3:
            return raw_text.strip(), tender_reference

        return "\n".join(captured_lines), tender_reference
