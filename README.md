# ai-powered-multi-agent-portfolio-website

A full‑stack AI‑powered portfolio website featuring a team of intelligent agents built with Python and React. Each agent specializes in navigation, projects, career insights, business services, and research, delivering real‑time, personalized interactions using modern LLM providers and secure authentication.

## Quick Start

See [SETUP.md](SETUP.md) for detailed setup instructions.

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Features

✅ **Secure Authentication** - Argon2 password hashing, JWT tokens, CSRF protection  
✅ **Rate Limiting** - Protection against brute force attacks  
✅ **Content Security** - CSP headers, sanitized markdown rendering  
✅ **Modern Stack** - FastAPI, Next.js 14, TypeScript, Tailwind CSS  
✅ **CI/CD Ready** - Automated security scanning with Bandit, Safety, pip-audit  
✅ **Dependabot** - Automated dependency updates  

## Documentation

- [SETUP.md](SETUP.md) - Complete setup and deployment guide
- API Docs: `http://localhost:8000/docs` (when backend is running)

## Security

This project implements security best practices from Phases 1-3:
- Argon2 password hashing
- CSRF protection
- Rate limiting on authentication endpoints
- Secure cookie handling (HttpOnly, Secure, SameSite)
- Content Security Policy headers
- XSS protection via markdown sanitization
- SQL injection prevention via ORM

For security issues, please see [SETUP.md](SETUP.md#security).

