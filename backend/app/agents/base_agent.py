from dataclasses import dataclass
from typing import List
from langchain_core.messages import SystemMessage, HumanMessage, BaseMessage
from app.services.llm_provider import LLMProvider

@dataclass
class AgentResponse:
    role: str
    content_md: str

class BaseAgent:
    name: str = "BaseAgent"
    system_preamble: str = "You are a helpful assistant. Reply in concise Markdown."

    def __init__(self):
        self.llm = LLMProvider()

    def _messages(self, user_query: str) -> List[BaseMessage]:
        return [
            SystemMessage(content=self.system_preamble),
            HumanMessage(content=user_query),
        ]

    def respond(self, user_query: str) -> AgentResponse:
        content = self.llm.invoke_text(self._messages(user_query))
        return AgentResponse(role=self.name, content_md=content)

    def stream(self, user_query: str):
        for chunk in self.llm.stream_text(self._messages(user_query)):
            yield chunk
