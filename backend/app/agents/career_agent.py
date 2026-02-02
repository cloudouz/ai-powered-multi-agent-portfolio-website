from app.agents.base_agent import BaseAgent

class CareerAgent(BaseAgent):
    name = "CareerAgent"
    system_preamble = (
        "You analyze skills and experience and map them to roles. Provide honest, actionable advice."
    )
