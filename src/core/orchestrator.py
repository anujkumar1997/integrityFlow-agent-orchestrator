
from __future__ import annotations

from ..agents.coding_agent import CodingAgent
from ..agents.explainer_agent import ExplainerAgent
from .guardrails import apply_guardrails
from .routers import route
from .types import AgentResponse, UserQuery

AGENTS = {
    "explainer": ExplainerAgent(),
    "coding": CodingAgent(),
}


def handle_query(text: str) -> AgentResponse:
    # 1) Wrap input
    query = UserQuery(text=text)

    # 2) Guardrails
    guardrail_result = apply_guardrails(query)
    if not guardrail_result.allowed:
        return AgentResponse(
            agent="guardrails",
            content="Blocked: " + "; ".join(guardrail_result.reasons),
            used_tools=[],
        )

    # 3) Use cleaned text (if guardrails produced it)
    cleaned_text = guardrail_result.cleaned_text or text

    # 4) Route
    route_decision = route(UserQuery(text=cleaned_text))

    # 5) Pick agent
    agent = AGENTS.get(route_decision.agent)
    if agent is None:
        return AgentResponse(
            agent="fallback",
            content=f"No agent wired for: {route_decision.agent}",
            used_tools=[],
        )

    # 6) Run agent (your agents accept UserQuery)
    cleaned_query = UserQuery(text=cleaned_text)
    return agent.run(cleaned_query)
