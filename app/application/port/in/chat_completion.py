from typing import Protocol

from app.application.dto.chat import ChatCompletionRequest, ChatCompletionResponse


class ChatCompletionInPort(Protocol):
    def execute(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        ...
