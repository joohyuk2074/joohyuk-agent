import os

from fastapi import FastAPI

from app.adapter.in.web.router import get_router
from app.adapter.out.llm.dummy_client import DummyLLMClient
from app.application.usecase.chat_completion import ChatCompletionUseCase


def create_app() -> FastAPI:
    app = FastAPI()

    model_name = os.getenv("LLM_MODEL_NAME", "dummy-model")
    llm_client = DummyLLMClient(model_name=model_name)
    usecase = ChatCompletionUseCase(llm_client=llm_client)

    app.include_router(get_router(usecase))
    return app


app = create_app()
