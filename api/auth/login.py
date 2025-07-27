"""Kullanıcı giriş endpointi örneği."""

from pydantic import BaseModel


class LoginRequest(BaseModel):
    """Giriş bilgileri"""
    username: str
    password: str


def login(data: LoginRequest) -> dict:
    """Başarılı girişte sahte token döner"""
    token = f"token_{data.username}"
    return {"access_token": token}
