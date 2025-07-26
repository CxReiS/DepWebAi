"""Auth endpointleri."""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.models.auth import LoginRequest, Token, UserCreate
from app.models.user import UserRead
from app.services.auth_service import authenticate, register_user
from app.database.session import get_db

router = APIRouter(prefix="/auth")


@router.post("/login", response_model=Token)
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db),
    lang: str = Query("en"),
):
    return authenticate(credentials, lang=lang, db=db)


@router.post("/register", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user)
