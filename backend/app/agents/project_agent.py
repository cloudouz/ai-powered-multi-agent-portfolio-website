from app.agents.base_agent import BaseAgent

class ProjectAgent(BaseAgent):
    name = "ProjectAgent"
    system_preamble = (
        "You answer technical questions about projects, architecture, and stacks. "
        "Return structured Markdown with headings and bullet points."
    )
