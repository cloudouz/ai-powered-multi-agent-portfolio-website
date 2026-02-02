import secrets
from fastapi import Response, Request, HTTPException, status
from app.core.config import settings

CSRF_COOKIE_NAME = "csrf_token"


def set_csrf_cookie(resp: Response) -> str:
    token = secrets.token_urlsafe(32)
    resp.set_cookie(
        CSRF_COOKIE_NAME,
        token,
        httponly=False,
        secure=(settings.ENV == "production"),
        samesite="Lax",
        max_age=3600,
        path="/",
    )
    return token


def verify_csrf(request: Request):
    cookie = request.cookies.get(CSRF_COOKIE_NAME)
    header = request.headers.get("X-CSRF-Token")
    if not cookie or not header or cookie != header:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid CSRF token")
