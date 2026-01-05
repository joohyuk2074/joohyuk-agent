from typing import List

from app.application.port.out.llm_client import LLMClientOutPort
from app.domain.model.chat import ChatMessage


class DummyLLMClient(LLMClientOutPort):
    def __init__(self, model_name: str) -> None:
        self._model_name = model_name

    def complete(self, messages: List[ChatMessage]) -> str:
        last = messages[-1].content if messages else ""
        return f"[{self._model_name}] echo: {last}"
