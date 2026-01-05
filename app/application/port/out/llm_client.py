from typing import List, Protocol

from app.domain.model.chat import ChatMessage


class LLMClientOutPort(Protocol):
    def complete(self, messages: List[ChatMessage]) -> str:
        ...
