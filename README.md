# AI‑Powered Multi‑Agent Portfolio Website (Python + React)

Production scaffold with:
- FastAPI backend + LangChain agents (Gemini primary, OpenAI fallback)
- Tavily web search tool for ResearchAgent
- Next.js frontend with TailwindCSS
- Docker + docker-compose, GitHub Actions CI

## Quickstart

### Prerequisites
- Python 3.11+
- Node 20+
- API keys: GEMINI_API_KEY (required for Gemini), optional OPENAI_API_KEY, TAVILY_API_KEY (required for research)

### Configure env
Copy env examples and fill in keys.

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

### Run locally (compose)
```bash
docker-compose up --build
```
- Backend: http://localhost:8000 (health: /healthz)
- Frontend: http://localhost:3000

### Run locally (manual)
Backend:
```bash
cd backend
pip install -e .
uvicorn app.main:app --reload
```
Frontend:
```bash
cd frontend
npm install
npm run dev
```

## API
- POST /api/welcome
- POST /api/projects
- POST /api/career
- POST /api/services
- POST /api/research
- POST /api/stream  (text stream demo)

## LLM Provider Selection
See docs/LLM_SETUP.md for details. Set `LLM_PROVIDER=gemini` (default) or `openai`.

## Security Notes
- JWT utilities and rate limiting are scaffolded. Add real auth flows and storage.
- Always set strong `JWT_SECRET` and serve over HTTPS in production.
- Configure CORS to your frontend domain.

## Deploy
- Backend: Render/Railway/Fly.io/AWS
- Frontend: Vercel/Netlify
- Set environment variables in the hosting provider.
