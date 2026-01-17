from __future__ import annotations

from .base import BaseAgent
from src.core.llm_client import chat
from src.core.types import UserQuery, AgentResponse


class CodingAgent(BaseAgent):
    name = "coding"

    def build_prompt(self, query: UserQuery) -> str:

        prompt = (
            "You are a coding agent. Your task is to provide clear and concise explanations "
            "to user queries. Use simple language and examples where appropriate.\n\n"
            f"User Query: {query.text}\n\n"
            "Explain the concept in detail:"
            "to user queries. Use simple language and examples where appropriate.\n\n"
            f"User Query: {query.text}\n\n"
            "Explain the concept in detail:"
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