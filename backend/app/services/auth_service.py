"""Kullanıcı doğrulama servisleri."""

from app.models.auth import LoginRequest, Token
from app.utils.helpers import get_message


def authenticate(credentials: LoginRequest, lang: str = "en") -> Token:
    """Basit doğrulama örneği."""
    if credentials.username == "admin" and credentials.password == "password":
        return Token(access_token="fake-token", message=get_message("login_success", lang))
    return Token(access_token="invalid", message=get_message("login_failed", lang))
