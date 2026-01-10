from __future__ import annotations
from typing import List
from .types import RouteDecision, UserQuery

CODING_KEYWORDS = {"code", "program", "function", "script", "algorithm","error","bug"}
CAREER_KEYWORDS = {"job", "career", "resume", "interview", "position"}
EXPLAINER_KEYWORDS = {"explain", "describe", "define", "what is", "how does"}


def count_keyword_hits(text: str, keywords: List[str]) -> List[str]:
    """
    Return a list of keywords that appear in the text.
    """
    hits = []
    lowered_text = text.lower()
    for kw in keywords:
        if kw in lowered_text:
            hits.append(kw)
    return hits


def route(query: UserQuery) -> RouteDecision:
    text = query.text.lower()

    coding_hits = count_keyword_hits(text, list(CODING_KEYWORDS))
    career_hits = count_keyword_hits(text, list(CAREER_KEYWORDS))
    explainer_hits = count_keyword_hits(text, list(EXPLAINER_KEYWORDS))

    buckets = {
        "coding": coding_hits,
        "career": career_hits,
        "explainer": explainer_hits,
    }

    agent, hits = max(buckets.items(), key=lambda x: len(x[1]))

    # No signal → fallback
    if len(hits) == 0:
        return RouteDecision(
            agent="fallback",
            confidence=0.3,
            reasons=["No routing keywords matched."],
        )

    # Simple confidence mapping (bounded)
    if len(hits) >= 3:
        confidence = 0.9
    elif len(hits) == 2:
        confidence = 0.8
    else:
        confidence = 0.7

    return RouteDecision(
        agent=agent,
        confidence=confidence,
        reasons=[f"Matched keywords: {hits}"],
    )
