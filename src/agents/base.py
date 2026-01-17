from __future__ import annotations
from abc import ABC, abstractmethod

from src.core.types import UserQuery, AgentResponse

class BaseAgent(ABC):
    """
    Base class for all agents.
    - Every agent must have a name
    - build a prompt
    - run and return AgentResponse
    """

    name: str

    @abstractmethod
    def build_prompt(self, query: UserQuery) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def run(self, query: UserQuery) -> AgentResponse:
        raise NotImplementedError
    