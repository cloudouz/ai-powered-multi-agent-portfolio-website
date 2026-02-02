# AI-Powered Multi-Agent Portfolio Website

A full‑stack AI‑powered portfolio website featuring a team of intelligent agents built with Python and React. Each agent specializes in navigation, projects, career insights, business services, and research, delivering real‑time, personalized interactions using modern LLM providers and secure authentication.

## Features

### Authentication & Security (Phases 1-3) ✅

- **Phase 1: Core Foundations**
  - Argon2 password hashing for secure password storage
  - Input validation via Pydantic
  - SQL injection prevention via SQLModel ORM
  - HTTPS-ready (configured at hosting layer)

- **Phase 2: Authentication & Session Security**
  - User model with unique email constraint
  - JWT-based authentication with secure cookie storage
  - Auth endpoints: register, login, logout, me, CSRF token issuer
  - Secure cookies (HttpOnly, Secure, SameSite=Lax)
  - Rate limiting on login (5 requests/minute)
  - Comprehensive auth failure logging

- **Phase 3: Frontend Protections**
  - CSRF token issuing and verification
  - Safe Markdown rendering with sanitization (GFM + rehype-sanitize)
  - Content Security Policy (CSP) headers
  - Security headers (X-Content-Type-Options, Referrer-Policy, Permissions-Policy)

## Tech Stack

### Backend
- **Framework**: FastAPI
- **Database**: SQLModel (SQLite by default, PostgreSQL-ready)
- **Authentication**: JWT (python-jose), Argon2 password hashing
- **Security**: SlowAPI rate limiting, CSRF protection
- **ORM**: SQLModel (Pydantic + SQLAlchemy)

### Frontend
- **Framework**: Next.js 14 (React)
- **Styling**: Tailwind CSS
- **Language**: TypeScript
- **Markdown**: react-markdown with sanitization

## Getting Started

### Prerequisites
- Python 3.11+
- Node.js 20+
- pip and npm

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy the environment example and configure:
```bash
cp .env.example .env
```

4. **Important**: Generate a secure JWT secret key:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```
Update `JWT_SECRET_KEY` in `.env` with the generated value.

5. Start the development server:
```bash
uvicorn app.main:app --reload --port 8000
```

The backend API will be available at http://localhost:8000

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Copy the environment example:
```bash
cp .env.example .env.local
```

4. Start the development server:
```bash
npm run dev
```

The frontend will be available at http://localhost:3000

## API Endpoints

### Health Check
- `GET /healthz` - Health check endpoint

### Authentication
- `POST /api/auth/csrf` - Issue CSRF token
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login (requires CSRF token)
- `POST /api/auth/logout` - Logout
- `GET /api/auth/me` - Get current user info

### Example Usage

1. **Get CSRF Token**:
```bash
curl -X POST http://localhost:8000/api/auth/csrf -c cookies.txt
```

2. **Register**:
```bash
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"securepass123"}'
```

3. **Login**:
```bash
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -H "X-CSRF-Token: <token_from_step_1>" \
  -b cookies.txt -c cookies.txt \
  -d '{"email":"user@example.com","password":"securepass123"}'
```

4. **Check Authentication**:
```bash
curl -X GET http://localhost:8000/api/auth/me -b cookies.txt
```

## Development

### Running Tests
```bash
# Backend tests (when implemented)
cd backend
pytest

# Frontend linting
cd frontend
npm run lint
```

### Building for Production

#### Backend
```bash
cd backend
# Use a production WSGI server like gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

#### Frontend
```bash
cd frontend
npm run build
npm run start
```

## Security

### Best Practices Implemented
- ✅ Argon2 password hashing
- ✅ JWT with HttpOnly cookies
- ✅ CSRF protection on state-changing endpoints
- ✅ Rate limiting on authentication
- ✅ Input validation with Pydantic
- ✅ SQL injection prevention with SQLModel
- ✅ XSS protection with sanitized Markdown
- ✅ CSP headers for browser security
- ✅ Secure cookie flags (HttpOnly, Secure, SameSite)

### Production Checklist
- [ ] Change `JWT_SECRET_KEY` to a secure random value
- [ ] Enable HTTPS at the hosting layer
- [ ] Configure proper CORS origins
- [ ] Use a production database (PostgreSQL recommended)
- [ ] Set up Redis for rate limiting (if using distributed deployment)
- [ ] Configure proper logging and monitoring
- [ ] Review and adjust rate limits based on usage

## CI/CD

The project includes GitHub Actions workflows for:
- **Backend**: Bandit security scanning, Safety vulnerability checks, pip-audit
- **Frontend**: ESLint, npm audit
- **Dependabot**: Automated dependency updates

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]
