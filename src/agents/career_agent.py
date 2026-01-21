from __future__ import annotations

from .base import BaseAgent
from src.core.llm_client import chat
from src.core.types import UserQuery, AgentResponse


class CarerAgent(BaseAgent):
    name = "career"

    def build_prompt(self, query: UserQuery) -> str:

        prompt = (
            "You are an career agent.  Use simple language and examples where appropriate.\n\n"
            f"User Query: {query.text}\n\n"
            "Explain the career paths in detail:"
        )
        return prompt
    
    def run(self, query: UserQuery) -> AgentResponse:
        prompt = self.build_prompt(query)
        response_text = chat(prompt)

        return AgentResponse(
            agent=self.name,
            content=response_text,
            used_tools=["llm"]
        )