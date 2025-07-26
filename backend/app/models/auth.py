"""Kimlik doğrulama şemaları."""

from pydantic import BaseModel


class LoginRequest(BaseModel):
    """Giriş bilgilerinin yapısı."""

    username: str
    password: str


class UserCreate(BaseModel):
    """Kullanıcı kayıt şeması."""

    username: str
    password: str


class Token(BaseModel):
    """Oluşturulan JWT."""

    access_token: str
    token_type: str = "bearer"
    message: str | None = None


class TokenData(BaseModel):
    """JWT içeriği."""

    sub: str | None = None
