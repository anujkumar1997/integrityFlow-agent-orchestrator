from __future__ import annotations

from .types import AgentResponse, UserQuery
from .guardrails import apply_guardrails
from .routers import route
from .tracer import Tracer

from ..agents.explainer_agent import ExplainerAgent
from ..agents.coding_agent import CodingAgent


AGENTS = {
    "explainer": ExplainerAgent(),
    "coding": CodingAgent(),
}


def handle_query(text: str, tracer: Tracer | None = None) -> AgentResponse:
    if tracer is None:
        tracer = Tracer()

    try:
        # 1) Wrap input
        query = UserQuery(text=text)

        # 2) Guardrails
        gr = apply_guardrails(query)
        if not gr.allowed:
            tracer.add(
                stage="guardrails",
                status="blocked",
                data={"reasons": gr.reasons},
            )
            return AgentResponse(
                agent="guardrails",
                content="Blocked: " + "; ".join(gr.reasons),
                used_tools=[],
            )

        tracer.add(
            stage="guardrails",
            status="ok",
            data={"cleaned": gr.cleaned_text is not None},
        )

        # 3) Cleaned text
        cleaned_text = gr.cleaned_text or text

        # 4) Router
        decision = route(UserQuery(text=cleaned_text))
        tracer.add(
            stage="router",
            status="ok",
            agent=decision.agent,
            data={"confidence": decision.confidence, "reasons": decision.reasons},
        )

        # 5) Pick agent
        agent = AGENTS.get(decision.agent)
        if agent is None:
            tracer.add(
                stage="orchestrator",
                status="fallback",
                agent=decision.agent,
                data={"reason": "agent_not_wired"},
            )
            return AgentResponse(
                agent="fallback",
                content=f"No agent wired for: {decision.agent}",
                used_tools=[],
            )

        # 6) Run agent (your agents accept UserQuery)
        tracer.add(stage="agent", status="ok", agent=agent.name, data={})
        return agent.run(UserQuery(text=cleaned_text))

    except Exception as e:
        tracer.add(
            stage="orchestrator",
            status="error",
            data={"error": str(e)},
        )
        return AgentResponse(
            agent="error",
            content="Internal error: " + str(e),
            used_tools=[],
        )
    


    
