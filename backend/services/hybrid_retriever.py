import json
import re
from typing import List, Dict, Any, Tuple, Optional
import numpy as np
from rank_bm25 import BM25Okapi
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from backend.config import STANDARDS_CATALOG_PATH, QCO_REGISTRY_PATH, SUPERSEDED_MAPPING_PATH
from backend.models.schemas import (
    StandardCatalogItem, StandardRecommendation, ClauseCitation, ExtractedParameters
)

class HybridRetriever:
    def __init__(self):
        self.standards: List[Dict[str, Any]] = self._load_standards()
        self.qco_map: Dict[str, Dict[str, Any]] = self._load_qco_map()
        self.superseded_map: Dict[str, Dict[str, Any]] = self._load_superseded()
        
        # Build search indexes
        self.corpus_texts = []
        self.tokenized_corpus = []
        
        for std in self.standards:
            # Combine code, title, scope, keywords, and clauses for indexing
            clause_texts = " ".join([f"{c['clause_title']} {c['content']}" for c in std.get("clauses", [])])
            keywords_text = " ".join(std.get("keywords", []))
            full_text = f"{std['is_code']} {std['title']} {std['scope']} {keywords_text} {clause_texts}"
            
            self.corpus_texts.append(full_text)
            self.tokenized_corpus.append(self._tokenize(full_text))

        # 1. BM25 Lexical Index
        self.bm25 = BM25Okapi(self.tokenized_corpus)
        
        # 2. Semantic TF-IDF Vectorizer
        self.tfidf_vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            stop_words='english',
            max_features=5000
        )
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.corpus_texts)

    def _load_standards(self) -> List[Dict[str, Any]]:
        if STANDARDS_CATALOG_PATH.exists():
            try:
                with open(STANDARDS_CATALOG_PATH, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def _load_qco_map(self) -> Dict[str, Dict[str, Any]]:
        qco_dict = {}
        if QCO_REGISTRY_PATH.exists():
            try:
                with open(QCO_REGISTRY_PATH, "r", encoding="utf-8") as f:
                    records = json.load(f)
                    for r in records:
                        for is_code in r.get("mandatory_standards", []):
                            qco_dict[is_code.strip()] = r
            except Exception:
                pass
        return qco_dict

    def _load_superseded(self) -> Dict[str, Dict[str, Any]]:
        if SUPERSEDED_MAPPING_PATH.exists():
            try:
                with open(SUPERSEDED_MAPPING_PATH, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {}

    def _tokenize(self, text: str) -> List[str]:
        # Lowercase alphanumeric tokenization
        tokens = re.findall(r'[a-zA-Z0-9]+', text.lower())
        return tokens

    def recommend(
        self,
        query_text: str,
        extracted: Optional[ExtractedParameters] = None,
        top_k: int = 4
    ) -> List[StandardRecommendation]:
        """Perform hybrid BM25 + Semantic search and return ranked standards with clause-level evidence."""
        
        # Tokenized query
        tokenized_query = self._tokenize(query_text)
        
        # 1. BM25 Lexical Scores
        bm25_scores = np.array(self.bm25.get_scores(tokenized_query))
        max_bm25 = np.max(bm25_scores) if len(bm25_scores) > 0 and np.max(bm25_scores) > 0 else 1.0
        normalized_bm25 = bm25_scores / max_bm25
        
        # 2. TF-IDF Semantic Cosine Similarity
        query_vec = self.tfidf_vectorizer.transform([query_text])
        cosine_scores = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        
        # 3. Direct Code / Parameter Overlap Boost
        boost_scores = np.zeros(len(self.standards))
        
        # Check if query references any superseded standard that leads to this standard
        superseded_warnings: Dict[int, str] = {}
        
        for idx, std in enumerate(self.standards):
            std_base = std.get("base_code", "")
            std_full = std.get("is_code", "")
            
            # Check for direct mentions of standard code in text
            if std_base.lower() in query_text.lower():
                boost_scores[idx] += 0.35

            # Check if tender cites an obsolete standard that this standard supersedes
            for old_code, meta in self.superseded_map.items():
                if old_code.lower() in query_text.lower():
                    if std_base.lower() in meta["superseded_by"].lower():
                        boost_scores[idx] += 0.45
                        superseded_warnings[idx] = (
                            f"Directly replaces '{old_code}' referenced in tender ({meta['reason']})"
                        )

            # Check for material grade overlap
            if extracted and extracted.material_grade:
                grades = [g.strip().lower() for g in extracted.material_grade.split(",")]
                for g in grades:
                    if g in " ".join(std.get("keywords", [])).lower() or g in std.get("scope", "").lower():
                        boost_scores[idx] += 0.20
                        break

            # Check for commodity overlap
            if extracted and extracted.commodity_name:
                comm_words = self._tokenize(extracted.commodity_name)
                match_count = sum(1 for w in comm_words if w in self.tokenized_corpus[idx])
                if len(comm_words) > 0:
                    boost_scores[idx] += 0.15 * (match_count / len(comm_words))

        # 4. Composite Match Score Formula
        # BM25: 35%, Semantic Cosine: 35%, Parameter/Superseded Boost: 30%
        composite_scores = (0.35 * normalized_bm25) + (0.35 * cosine_scores) + (0.30 * boost_scores)
        
        # Top-K ranking
        ranked_indices = np.argsort(composite_scores)[::-1][:top_k]
        
        recommendations: List[StandardRecommendation] = []
        for idx in ranked_indices:
            raw_score = composite_scores[idx]
            # Convert to 0-100 percentage scale
            match_score = float(min(98.5, max(25.0, round(raw_score * 100, 1))))
            
            std = self.standards[idx]
            is_base = std.get("base_code", "")
            
            # Determine match confidence tier
            if match_score >= 75.0:
                confidence = "HIGH"
            elif match_score >= 50.0:
                confidence = "MEDIUM"
            else:
                confidence = "LOW"
                
            # QCO status
            is_qco = std.get("mandatory_qco", False) or (is_base in self.qco_map)
            qco_min = std.get("qco_ministry")
            if not qco_min and is_base in self.qco_map:
                qco_min = self.qco_map[is_base].get("issuing_ministry")
                
            # Clause citations & explainability alignment
            citations, reasons = self._align_clauses(std, query_text, extracted)
            
            # Add superseded alert if present
            superseded_alert = superseded_warnings.get(idx)

            recommendations.append(StandardRecommendation(
                is_code=std["is_code"],
                base_code=is_base,
                title=std["title"],
                publication_year=std["publication_year"],
                reaffirmed_year=std.get("reaffirmed_year"),
                division_name=std["division_name"],
                status=std["status"],
                match_score=match_score,
                match_confidence=confidence,
                mandatory_qco=is_qco,
                qco_ministry=qco_min,
                superseded_warning=superseded_alert,
                scope_summary=std["scope"][:250] + "..." if len(std["scope"]) > 250 else std["scope"],
                clause_citations=citations,
                key_reasons=reasons
            ))
            
        return recommendations

    def _align_clauses(
        self,
        standard: Dict[str, Any],
        query_text: str,
        extracted: Optional[ExtractedParameters]
    ) -> Tuple[List[ClauseCitation], List[str]]:
        citations: List[ClauseCitation] = []
        reasons: List[str] = []
        
        clauses = standard.get("clauses", [])
        lower_query = query_text.lower()
        
        for c in clauses:
            c_text = (c["clause_title"] + " " + c["content"]).lower()
            matching_points = []
            
            # Check grade matching
            if extracted and extracted.material_grade:
                for g in extracted.material_grade.split(","):
                    clean_g = g.strip().lower()
                    if clean_g and clean_g in c_text:
                        matching_points.append(f"Governs specified Grade '{g.strip()}'")
            
            # Check ratings / properties
            if extracted:
                for r in extracted.mechanical_ratings:
                    # check for numeric match
                    num = re.search(r'\d+', r)
                    if num and num.group(0) in c_text:
                        matching_points.append(f"Specifies exact rating limit ({r})")
                        break
                        
                for t in extracted.testing_requirements:
                    t_words = self._tokenize(t)
                    if any(w in c_text for w in t_words if len(w) > 3):
                        matching_points.append(f"Prescribes procedure for {t}")
                        break
                        
            # If matching points found, record citation
            if matching_points:
                alignment = "; ".join(matching_points)
                citations.append(ClauseCitation(
                    clause_number=c["clause_number"],
                    clause_title=c["clause_title"],
                    alignment_reason=alignment,
                    standard_text_snippet=c["content"]
                ))
                reasons.append(f"{c['clause_number']} ({c['clause_title']}): {alignment}")
                
        # If no specific clauses matched, provide default scope alignment
        if not reasons:
            reasons.append(f"Scope directly covers technical requirements for '{standard['title']}'.")
            if clauses:
                citations.append(ClauseCitation(
                    clause_number=clauses[0]["clause_number"],
                    clause_title=clauses[0]["clause_title"],
                    alignment_reason="Standard scope and technical requirements encompass the required procurement item.",
                    standard_text_snippet=clauses[0]["content"]
                ))

        return citations[:3], reasons[:3]
