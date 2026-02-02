from app.agents.base_agent import BaseAgent

class BusinessAdvisor(BaseAgent):
    name = "BusinessAdvisor"
    system_preamble = (
        "You recommend services, pricing, and proposal structures. Be clear about assumptions."
    )
