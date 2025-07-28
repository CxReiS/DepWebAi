"""Kullanıcı kimlik doğrulama servisleri."""

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import jwt

from app.models.auth import LoginRequest, Token, TokenData, UserCreate
from app.models.user import UserORM, UserRead
from app.core import security
from app.database.session import SessionLocal
from app.core.config import settings
from app.core.helpers import get_message
import os


def authenticate(
    credentials: LoginRequest, lang: str = "en", db: Session | None = None
) -> Token:
    close_db = False
    if db is None:
        db = SessionLocal()
        close_db = True
    try:
        user = (
            db.query(UserORM).filter(UserORM.username == credentials.username).first()
        )
        if user is None and credentials.username == os.environ.get(
            "ADMIN_USER", "admin"
        ):
            hashed = security.get_password_hash(
                os.environ.get("ADMIN_PASS", "password")
            )
            user = UserORM(username=credentials.username, hashed_password=hashed)
            db.add(user)
            db.commit()
            db.refresh(user)
        if user and security.verify_password(
            credentials.password, user.hashed_password
        ):
            message = get_message("auth.login_success", lang)
        else:
            message = get_message("auth.login_failed", lang)
        token = security.create_access_token({"sub": str(user.id) if user else "0"})
        return Token(access_token=token, message=message)
    finally:
        if close_db:
            db.close()


def register_user(db: Session, new_user: UserCreate) -> UserRead:
    if db.query(UserORM).filter(UserORM.username == new_user.username).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Kullanıcı mevcut"
        )
    hashed = security.get_password_hash(new_user.password)
    user = UserORM(username=new_user.username, hashed_password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return UserRead.model_validate(user)


def decode_token(token: str) -> TokenData:
    """JWT'i çözümler."""
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        return TokenData(sub=str(payload.get("sub")))
    except jwt.PyJWTError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Geçersiz token") from exc


def get_current_user(db: Session, token: str) -> UserRead:
    """Token'dan kullanıcıyı getirir."""
    data = decode_token(token)
    if not data.sub:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Geçersiz token")
    user = db.query(UserORM).get(int(data.sub))
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Kullanıcı bulunamadı")
    return UserRead.model_validate(user)
