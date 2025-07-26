"""Kullanıcı işlemleri."""

from fastapi import APIRouter
from app.models.user import User

router = APIRouter()

fake_users_db = [
    {"id": 1, "username": "alice"},
    {"id": 2, "username": "bob"},
]

@router.get("/", response_model=list[User])
def list_users():
    """Kayıtlı kullanıcıları döndürür."""
    return fake_users_db
