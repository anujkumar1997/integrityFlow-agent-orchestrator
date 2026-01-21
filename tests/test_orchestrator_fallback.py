from src.core.orchestrator import handle_query
from src.core.tracer import Tracer

def test_orchestrator_fallback_for_career():
    tracer = Tracer()
    r = handle_query("help me with my resume interview", tracer=tracer)
    assert r.agent == "fallback"