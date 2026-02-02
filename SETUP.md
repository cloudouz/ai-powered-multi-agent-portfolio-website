# AI-Powered Multi-Agent Portfolio Website

A full‑stack AI‑powered portfolio website featuring a team of intelligent agents built with Python and React. Each agent specializes in navigation, projects, career insights, business services, and research, delivering real‑time, personalized interactions using modern LLM providers and secure authentication.

## Features

### Security & Authentication (Phases 1-3)

#### Phase 1: Core Foundations
- **Argon2 Password Hashing**: Industry-standard password hashing using argon2-cffi
- **Input Validation**: Pydantic models for robust data validation
- **SQL Injection Prevention**: SQLModel ORM for safe database operations
- **HTTPS Ready**: Configured for secure deployment (at hosting layer)

#### Phase 2: Authentication & Session Security
- **User Management**: SQLModel-based user system with email/password authentication
- **JWT Tokens**: Secure, short-lived access tokens stored in HttpOnly cookies
- **CSRF Protection**: Token-based CSRF protection for state-changing operations
- **Rate Limiting**: Login endpoint rate-limited to 5 attempts per minute
- **Secure Cookies**: HttpOnly, Secure, SameSite=Lax cookie configuration
- **Auth Endpoints**: Complete authentication flow (register, login, logout, me, csrf)

#### Phase 3: Frontend Protections
- **Content Security Policy**: Comprehensive CSP headers to prevent XSS attacks
- **Safe Markdown Rendering**: GitHub-flavored markdown with HTML sanitization
- **Security Headers**: X-Content-Type-Options, Referrer-Policy, Permissions-Policy
- **CSRF Integration**: Client-side CSRF token handling in login flow

#### DevOps & CI
- **Dependabot**: Automated dependency updates for Python and npm packages
- **Security Scanning**: Bandit, Safety, and pip-audit in CI pipeline
- **Automated Testing**: CI workflow for backend and frontend validation

## Tech Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **SQLModel**: SQL databases with Python type hints
- **Argon2**: Secure password hashing
- **python-jose**: JWT token creation and validation
- **slowapi**: Rate limiting middleware
- **Pydantic**: Data validation using Python type annotations

### Frontend
- **Next.js 14**: React framework with server-side rendering
- **TypeScript**: Type-safe JavaScript
- **Tailwind CSS**: Utility-first CSS framework
- **react-markdown**: Markdown rendering with sanitization
- **rehype-sanitize**: HTML sanitization for XSS protection

## Getting Started

### Prerequisites
- Python 3.11+
- Node.js 20+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create environment configuration:
```bash
cp .env.example .env
# Edit .env and set your configuration
```

5. Start the development server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`
- API docs: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/healthz`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create environment configuration:
```bash
cp .env.local.example .env.local
# Edit .env.local and set NEXT_PUBLIC_API_URL=http://localhost:8000
```

4. Start the development server:
```bash
npm run dev
```

The application will be available at `http://localhost:3000`

### Building for Production

#### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

#### Frontend
```bash
cd frontend
npm run build
npm start
```

## API Endpoints

### Authentication
- `POST /api/auth/csrf` - Issue CSRF token
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login (requires CSRF token)
- `POST /api/auth/logout` - Logout
- `GET /api/auth/me` - Get current user status

### Health
- `GET /healthz` - Health check endpoint
- `GET /api/health` - API health check

## Security Features

### Password Security
- Passwords hashed with Argon2 (winner of Password Hashing Competition)
- Minimum password length: 8 characters
- Maximum password length: 128 characters

### Session Security
- JWT tokens expire after 30 minutes
- Tokens stored in HttpOnly cookies (not accessible via JavaScript)
- Secure flag ensures cookies only sent over HTTPS
- SameSite=Lax prevents CSRF attacks

### CSRF Protection
- CSRF tokens required for state-changing operations
- Tokens validated on login endpoint
- Token mismatch returns 403 Forbidden

### Rate Limiting
- Login endpoint limited to 5 attempts per minute per IP
- Rate limit exceeded returns 429 Too Many Requests

### Content Security
- CSP headers prevent XSS attacks
- Markdown content sanitized to remove dangerous HTML
- X-Content-Type-Options prevents MIME sniffing
- Permissions-Policy restricts browser features

## Environment Variables

### Backend (.env)
```
API_PREFIX=/api
CORS_ORIGINS=http://localhost:3000
DATABASE_URL=sqlite:///./app.db
JWT_SECRET=change-me-in-production-use-a-long-random-string
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=30
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Development

### Running Tests

#### Backend
```bash
cd backend
pytest
```

#### Frontend
```bash
cd frontend
npm test
```

### Linting

#### Backend
```bash
cd backend
bandit -r app
```

#### Frontend
```bash
cd frontend
npm run lint
```

### Security Scanning

#### Backend
```bash
cd backend
bandit -r app
safety check
pip-audit
```

#### Frontend
```bash
cd frontend
npm audit
```

## Project Structure

```
.
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth_routes.py    # Authentication endpoints
│   │   │   └── routes.py         # General API routes
│   │   ├── core/
│   │   │   └── config.py         # Configuration settings
│   │   ├── models/
│   │   │   └── user.py           # User database model
│   │   ├── security/
│   │   │   ├── auth.py           # JWT token handling
│   │   │   ├── csrf.py           # CSRF protection
│   │   │   ├── passwords.py      # Password hashing
│   │   │   └── rate_limit.py     # Rate limiting
│   │   ├── db.py                 # Database setup
│   │   └── main.py               # FastAPI application
│   ├── requirements.txt          # Python dependencies
│   └── .env.example              # Environment template
├── frontend/
│   ├── app/
│   │   ├── login/
│   │   │   └── page.tsx          # Login page
│   │   ├── globals.css           # Global styles
│   │   ├── layout.tsx            # Root layout
│   │   └── page.tsx              # Home page
│   ├── components/
│   │   └── MarkdownView.tsx      # Safe markdown renderer
│   ├── next.config.js            # Next.js config with CSP
│   ├── package.json              # npm dependencies
│   └── .env.local.example        # Environment template
├── .github/
│   ├── dependabot.yml            # Dependency updates
│   └── workflows/
│       └── ci.yml                # CI/CD pipeline
├── .gitignore
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linters
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Security

If you discover a security vulnerability, please email security@example.com instead of using the issue tracker.

## Deployment

### Recommended Hosting
- Backend: Railway, Render, Fly.io, or AWS
- Frontend: Vercel, Netlify, or CloudFlare Pages
- Database: PostgreSQL on Railway, Supabase, or AWS RDS

### Production Checklist
- [ ] Set strong JWT_SECRET (use secrets.token_urlsafe(64))
- [ ] Use PostgreSQL instead of SQLite for production
- [ ] Enable HTTPS at hosting layer
- [ ] Set secure CORS_ORIGINS (not "*")
- [ ] Configure proper CSP headers for your domain
- [ ] Enable rate limiting at load balancer level
- [ ] Set up database backups
- [ ] Configure monitoring and logging
- [ ] Review and update security headers
- [ ] Run security scanners in CI/CD

## Support

For questions and support, please open an issue on GitHub.
