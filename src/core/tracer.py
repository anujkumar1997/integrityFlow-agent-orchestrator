from __future__ import annotations

import time
from typing import Any, Dict, List, Literal, Optional

from .types import TraceEvent


class Tracer:
    def __init__(self) -> None:
        self.events: List[TraceEvent] = []

    def add(
        self,
        stage: Literal["guardrails", "router", "agent", "orchestrator"],
        status: Literal["ok", "blocked", "error", "fallback"],
        agent: Optional[str] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> None:
        event = TraceEvent(
            timestamp=time.time(),
            stage=stage,
            status=status,
            agent=agent,
            data=data or {},
        )
        self.events.append(event)
