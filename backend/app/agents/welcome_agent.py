from app.agents.base_agent import BaseAgent

class WelcomeAgent(BaseAgent):
    name = "WelcomeAgent"
    system_preamble = (
        "You are the site guide. Help users navigate pages, explain content, and suggest next steps. "
        "Always reply in concise Markdown."
    )
