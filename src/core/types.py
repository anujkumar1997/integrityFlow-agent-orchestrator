from __future__ import annotations

from typing import Any, Dict, List, Optional, Literal
from pydantic import BaseModel, Field


class UserQuery(BaseModel):
    text: str = Field(..., min_length=1, max_length=4000)
    user_id: str = Field(default="anonymous")
    metadata: Dict[str, Any] = Field(default_factory=dict)


class GuardrailResult(BaseModel):
    allowed: bool
    reasons: List[str] = Field(default_factory=list)
    cleaned_text: Optional[str] = None

class RouteDecision(BaseModel):
    agent: Literal["coding", "career", "explainer", "fallback"]
    confidence: float = Field(..., ge=0.0, le=1.0)
    reasons: List[str] = Field(default_factory=list)





