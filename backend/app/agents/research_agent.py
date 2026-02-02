import json
from typing import List
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage, BaseMessage
from app.agents.base_agent import BaseAgent, AgentResponse
from app.services.llm_provider import LLMProvider
from app.core.config import settings
from langchain_community.tools.tavily_search import TavilySearchResults

class ResearchAgent(BaseAgent):
    name = "ResearchAgent"
    system_preamble = (
        "You synthesize web research into concise insights with citations. "
        "Prefer recent, reputable sources. Always cite URLs at the end."
    )

    def __init__(self):
        super().__init__()
        if not settings.TAVILY_API_KEY:
            raise RuntimeError("TAVILY_API_KEY not set")
        self.search_tool = TavilySearchResults(max_results=5)

    async def research(self, user_query: str) -> AgentResponse:
        messages: List[BaseMessage] = [
            SystemMessage(content=self.system_preamble + "\nUse the tavily_search tool when web data is needed."),
            HumanMessage(content=user_query),
        ]
        tool_bound = self.llm.bind_tools([self.search_tool])
        ai_msg: AIMessage = tool_bound.invoke(messages)
        messages.append(ai_msg)

        if getattr(ai_msg, "tool_calls", None):
            for tc in ai_msg.tool_calls:
                if tc["name"] == self.search_tool.name:
                    args = tc.get("args", {}) or {}
                    result = self.search_tool.invoke(args)
                    messages.append(ToolMessage(content=json.dumps(result), tool_call_id=tc["id"]))
            final_msg: AIMessage = self.llm.get_model().invoke(messages)
            content = final_msg.content if isinstance(final_msg, AIMessage) else str(final_msg)
        else:
            content = ai_msg.content

        return AgentResponse(role=self.name, content_md=content or "No content.")
