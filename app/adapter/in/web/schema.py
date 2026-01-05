from typing import List

from pydantic import BaseModel, Field


class ChatMessageSchema(BaseModel):
    role: str = Field(..., examples=["user"])
    content: str


class ChatCompletionRequestSchema(BaseModel):
    messages: List[ChatMessageSchema]


class ChatCompletionResponseSchema(BaseModel):
    content: str
