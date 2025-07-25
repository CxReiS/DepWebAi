"""Kullanıcı kimlik doğrulama işlemleri."""

from fastapi import APIRouter, Query
from app.models.auth import LoginRequest, Token
from app.services.auth_service import authenticate
from app.utils.helpers import get_message

router = APIRouter()

@router.post("/login", response_model=Token)
def login(credentials: LoginRequest, lang: str = Query("en")):
    """Giriş endpointi"""
    return authenticate(credentials, lang)

@router.post("/register")
def register(user: LoginRequest, lang: str = Query("en")):
    """Kayıt endpointi sadece örnek"""
    return {"message": get_message("user_registered", lang), "user": user.username}
