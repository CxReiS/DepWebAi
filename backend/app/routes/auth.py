"""Kullanıcı kimlik doğrulama işlemleri."""

from fastapi import APIRouter, Depends
from app.models.auth import LoginRequest, Token
from app.services.auth_service import authenticate

router = APIRouter()

@router.post("/login", response_model=Token)
def login(credentials: LoginRequest):
    """Giriş endpointi"""
    return authenticate(credentials)

@router.post("/register")
def register(user: LoginRequest):
    """Kayıt endpointi sadece örnek"""
    return {"user": user.username}
