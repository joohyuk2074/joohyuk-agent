from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class ChatMessage:
    role: str
    content: str


@dataclass(frozen=True)
class ChatCompletionResult:
    content: str
    messages: List[ChatMessage]
