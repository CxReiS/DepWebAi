"""Kullanıcı CRUD servisleri."""

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.user import UserCreate, UserORM, UserRead
from app.core import security


def create_user(db: Session, data: UserCreate) -> UserRead:
    if db.query(UserORM).filter_by(username=data.username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Kullanıcı mevcut")
    user = UserORM(username=data.username, hashed_password=security.get_password_hash(data.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return UserRead.model_validate(user)


def get_user(db: Session, user_id: int) -> UserRead:
    user = db.query(UserORM).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bulunamadı")
    return UserRead.model_validate(user)


def list_users(db: Session) -> list[UserRead]:
    return [UserRead.model_validate(u) for u in db.query(UserORM).all()]
