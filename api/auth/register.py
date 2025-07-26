"""Kullanıcı kayıt endpointi örneği."""

from pydantic import BaseModel

users: dict[str, str] = {}


class RegisterRequest(BaseModel):
    """Kayıt bilgileri"""
    username: str
    password: str


def register(data: RegisterRequest) -> dict:
    """Yeni kullanıcı ekler"""
    if data.username in users:
        return {"success": False}
    users[data.username] = data.password
    return {"success": True}
