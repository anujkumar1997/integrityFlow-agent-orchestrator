from src.core.types import UserQuery
from src.core.routers import route


def test_routes_to_coding():
    d = route(UserQuery(text="python traceback error"))
    assert d.agent == "coding"
    assert d.confidence >= 0.7


def test_routes_to_career():
    d = route(UserQuery(text="resume interview job"))
    assert d.agent == "career"
    assert d.confidence >= 0.7


def test_routes_to_explainer():
    d = route(UserQuery(text="explain what guardrails are"))
    assert d.agent == "explainer"


def test_routes_to_fallback():
    d = route(UserQuery(text="tell me a joke"))
    assert d.agent == "fallback"
