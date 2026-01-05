from app.application.dto.chat import ChatCompletionRequest
from app.application.usecase.chat_completion import ChatCompletionUseCase
from app.domain.model.chat import ChatMessage


class FakeLLMClient:
    def complete(self, messages):
        return "ok"


def test_chat_completion_usecase_returns_content():
    usecase = ChatCompletionUseCase(llm_client=FakeLLMClient())
    request = ChatCompletionRequest(messages=[ChatMessage(role="user", content="hi")])

    result = usecase.execute(request)

    assert result.content == "ok"
