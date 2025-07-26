"""Kullanıcı doğrulama servisleri."""

import os
from uuid import uuid4

from app.models.auth import LoginRequest, Token
from app.utils.helpers import get_message


ADMIN_USER = os.environ.get("ADMIN_USER", "admin")
ADMIN_PASS = os.environ.get("ADMIN_PASS", "password")


def authenticate(credentials: LoginRequest, lang: str = "en") -> Token:
    """Basit doğrulama örneği."""
    if credentials.username == ADMIN_USER and credentials.password == ADMIN_PASS:
        return Token(access_token=str(uuid4()), message=get_message("login_success", lang))
    return Token(access_token=str(uuid4()), message=get_message("login_failed", lang))
