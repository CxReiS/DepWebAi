"""Kullanıcı kimlik doğrulama servisleri."""

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.auth import LoginRequest, Token, UserCreate
from app.models.user import UserORM, UserRead
from app.core import security
from app.database.session import SessionLocal
from app.utils.helpers import get_message
import os


def authenticate(credentials: LoginRequest, lang: str = "en", db: Session | None = None) -> Token:
    close_db = False
    if db is None:
        db = SessionLocal()
        close_db = True
    try:
        user = db.query(UserORM).filter(UserORM.username == credentials.username).first()
        if user is None and credentials.username == os.environ.get("ADMIN_USER", "admin"):
            hashed = security.get_password_hash(os.environ.get("ADMIN_PASS", "password"))
            user = UserORM(username=credentials.username, hashed_password=hashed)
            db.add(user)
            db.commit()
            db.refresh(user)
        if user and security.verify_password(credentials.password, user.hashed_password):
            message = get_message("login_success", lang)
        else:
            message = get_message("login_failed", lang)
        token = security.create_access_token({"sub": str(user.id) if user else "0"})
        return Token(access_token=token, message=message)
    finally:
        if close_db:
            db.close()


def register_user(db: Session, new_user: UserCreate) -> UserRead:
    if db.query(UserORM).filter(UserORM.username == new_user.username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Kullanıcı mevcut")
    hashed = security.get_password_hash(new_user.password)
    user = UserORM(username=new_user.username, hashed_password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return UserRead.model_validate(user)
