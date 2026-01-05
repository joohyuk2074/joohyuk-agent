from dataclasses import dataclass
from typing import List

from app.domain.model.chat import ChatMessage


@dataclass(frozen=True)
class ChatCompletionRequest:
    messages: List[ChatMessage]


@dataclass(frozen=True)
class ChatCompletionResponse:
    content: str
