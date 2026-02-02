from fastapi import APIRouter, Depends, HTTPException, Response, Request, status
from pydantic import BaseModel, EmailStr, constr
from sqlmodel import select
from sqlmodel import Session
from app.db import get_session
from app.models.user import User
from app.security.passwords import hash_password, verify_password
from app.security.auth import create_access_token
from app.security.rate_limit import limiter
from app.security.csrf import set_csrf_cookie, verify_csrf

router = APIRouter()

class RegisterIn(BaseModel):
    email: EmailStr
    password: constr(min_length=8, max_length=128)


class LoginIn(BaseModel):
    email: EmailStr
    password: constr(min_length=8, max_length=128)


@router.post("/auth/csrf")
def issue_csrf(response: Response):
    token = set_csrf_cookie(response)
    return {"csrf_token": token}


@router.post("/auth/register", status_code=201)
def register(payload: RegisterIn, session: Session = Depends(get_session)):
    exists = session.exec(select(User).where(User.email == payload.email)).first()
    if exists:
        raise HTTPException(status_code=409, detail="Email already registered")
    u = User(email=payload.email, password_hash=hash_password(payload.password))
    session.add(u)
    session.commit()
    session.refresh(u)
    return {"id": u.id, "email": u.email}


@router.post("/auth/login")
@limiter.limit("5/minute")
def login(payload: LoginIn, request: Request, response: Response, session: Session = Depends(get_session)):
    # CSRF check
    verify_csrf(request)

    user = session.exec(select(User).where(User.email == payload.email)).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(sub=str(user.id), role=user.role)
    response.set_cookie(
        "access_token",
        token,
        httponly=True,
        secure=True,
        samesite="Lax",
        max_age=1800,
        path="/",
    )
    return {"ok": True}


@router.post("/auth/logout")
def logout(response: Response):
    response.delete_cookie("access_token", path="/")
    return {"ok": True}


@router.get("/auth/me")
def me(request: Request):
    authed = bool(request.cookies.get("access_token"))
    return {"authenticated": authed}
