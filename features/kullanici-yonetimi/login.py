"""Kullanıcı giriş işlemleri."""

from .register import users

def login(username: str, password: str) -> bool:
    """Kayıtlı kullanıcıyı doğrular"""
    return users.get(username) == password

