"""Auth ile ilgili Pydantic şemalar."""

from pydantic import BaseModel

class LoginRequest(BaseModel):
    """Giriş için kullanıcı bilgileri"""
    username: str
    password: str

class Token(BaseModel):
    """JWT token ve mesaj."""
    access_token: str
    message: str
