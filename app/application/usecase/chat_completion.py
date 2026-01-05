from app.application.dto.chat import ChatCompletionRequest, ChatCompletionResponse
from app.application.port.in.chat_completion import ChatCompletionInPort
from app.application.port.out.llm_client import LLMClientOutPort


class ChatCompletionUseCase(ChatCompletionInPort):
    def __init__(self, llm_client: LLMClientOutPort) -> None:
        self._llm_client = llm_client

    def execute(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        content = self._llm_client.complete(request.messages)
        return ChatCompletionResponse(content=content)
