"""Kullanıcı doğrulama servisleri."""

from app.models.auth import LoginRequest, Token


def authenticate(credentials: LoginRequest) -> Token:
    """Basit doğrulama örneği."""
    if credentials.username == "admin" and credentials.password == "password":
        return Token(access_token="fake-token")
    return Token(access_token="invalid")
