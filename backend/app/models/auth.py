"""Auth ile ilgili Pydantic şemalar."""

from pydantic import BaseModel

class LoginRequest(BaseModel):
    """Giriş için kullanıcı bilgileri"""
    username: str
    password: str

class Token(BaseModel):
    """JWT token örneği"""
    access_token: str
