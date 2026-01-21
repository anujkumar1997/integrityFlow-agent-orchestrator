from src.core.orchestrator import handle_query
from src.core.tracer import Tracer

def test_tracing_includes_router_event():
    tracer = Tracer()
    _ = handle_query("explain what routing is", tracer=tracer)

    stages = [e.stage for e in tracer.events]
    assert "guardrails" in stages
    assert "router" in stages
