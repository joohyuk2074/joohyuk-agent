from typing import List

from fastapi import APIRouter

from app.adapter.in.web.schema import (
    ChatCompletionRequestSchema,
    ChatCompletionResponseSchema,
    ChatMessageSchema,
)
from app.application.dto.chat import ChatCompletionRequest
from app.application.port.in.chat_completion import ChatCompletionInPort
from app.domain.model.chat import ChatMessage


def _to_domain_messages(messages: List[ChatMessageSchema]) -> List[ChatMessage]:
    return [ChatMessage(role=m.role, content=m.content) for m in messages]


def get_router(usecase: ChatCompletionInPort) -> APIRouter:
    router = APIRouter()

    @router.post("/v1/chat/completions", response_model=ChatCompletionResponseSchema)
    def chat_completion(payload: ChatCompletionRequestSchema) -> ChatCompletionResponseSchema:
        request = ChatCompletionRequest(messages=_to_domain_messages(payload.messages))
        result = usecase.execute(request)
        return ChatCompletionResponseSchema(content=result.content)

    @router.get("/v1/models")
    def list_models() -> dict:
        return {"models": ["dummy-model"]}

    return router
