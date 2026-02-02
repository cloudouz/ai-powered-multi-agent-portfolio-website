from fastapi import APIRouter, Response, Request
from pydantic import BaseModel, Field
from app.agents.welcome_agent import WelcomeAgent
from app.agents.project_agent import ProjectAgent
from app.agents.career_agent import CareerAgent
from app.agents.business_agent import BusinessAdvisor
from app.agents.research_agent import ResearchAgent
from app.security.rate_limit import limiter
from fastapi.responses import StreamingResponse

router = APIRouter()

class Query(BaseModel):
    query: str = Field(..., min_length=1, max_length=2000)

@router.post("/welcome")
@limiter.limit("30/minute")
def welcome(payload: Query, request: Request, resp: Response):
    agent = WelcomeAgent()
    r = agent.respond(payload.query)
    return {"agent": r.role, "markdown": r.content_md}

@router.post("/projects")
@limiter.limit("30/minute")
def projects(payload: Query, request: Request, resp: Response):
    agent = ProjectAgent()
    r = agent.respond(payload.query)
    return {"agent": r.role, "markdown": r.content_md}

@router.post("/career")
@limiter.limit("20/minute")
def career(payload: Query, request: Request, resp: Response):
    agent = CareerAgent()
    r = agent.respond(payload.query)
    return {"agent": r.role, "markdown": r.content_md}

@router.post("/services")
@limiter.limit("20/minute")
def services(payload: Query, request: Request, resp: Response):
    agent = BusinessAdvisor()
    r = agent.respond(payload.query)
    return {"agent": r.role, "markdown": r.content_md}

@router.post("/research")
@limiter.limit("15/minute")
async def research(payload: Query, request: Request, resp: Response):
    agent = ResearchAgent()
    r = await agent.research(payload.query)
    return {"agent": r.role, "markdown": r.content_md}

@router.post("/stream")
def stream(payload: Query, request: Request):
    agent = WelcomeAgent()
    def gen():
        for chunk in agent.stream(payload.query):
            yield chunk
    return StreamingResponse(gen(), media_type="text/plain")
