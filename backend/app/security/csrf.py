import secrets
from fastapi import Response
from app.core.config import settings

CSRF_COOKIE_NAME = "csrf_token"

def set_csrf_cookie(resp: Response):
    token = secrets.token_urlsafe(32)
    resp.set_cookie(
        CSRF_COOKIE_NAME, token, httponly=False, 
        secure=(settings.ENV == "production"), 
        samesite="Lax", max_age=3600
    )
    return token
