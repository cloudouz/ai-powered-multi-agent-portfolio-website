from typing import Iterable, List
from app.core.config import settings
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import BaseMessage
from langchain_core.outputs import ChatGeneration, ChatResult

# Providers
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

class LLMProvider:
    def __init__(self, temperature: float = 0.2):
        self.temperature = temperature
        self._model = self._build_model()

    def _build_model(self) -> BaseChatModel:
        provider = (settings.LLM_PROVIDER or "gemini").lower()
        if provider == "openai":
            if not settings.OPENAI_API_KEY:
                raise RuntimeError("OPENAI_API_KEY not set")
            return ChatOpenAI(
                model="gpt-4o-mini",
                temperature=self.temperature,
                api_key=settings.OPENAI_API_KEY,
            )
        # default: gemini
        if not settings.GEMINI_API_KEY:
            raise RuntimeError("GEMINI_API_KEY not set")
        return ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            temperature=self.temperature,
            google_api_key=settings.GEMINI_API_KEY,
        )

    def get_model(self) -> BaseChatModel:
        return self._model

    def invoke_text(self, messages: List[BaseMessage]) -> str:
        result: ChatResult = self._model.invoke(messages)
        if not result.generations:
            return ""
        gen: ChatGeneration = result.generations[0]
        content = gen.text if hasattr(gen, "text") else gen.message.content
        return content or ""

    def stream_text(self, messages: List[BaseMessage]) -> Iterable[str]:
        try:
            for chunk in self._model.stream(messages):
                text = getattr(chunk, "text", None) or getattr(chunk, "content", None)
                if text:
                    yield str(text)
        except TypeError:
            yield self.invoke_text(messages)

    def bind_tools(self, tools):
        return self._model.bind_tools(tools)
