"""Kullanıcı endpointleri."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.user import UserCreate, UserRead
from app.services.user_service import create_user, get_user, list_users
from app.database.session import get_db

router = APIRouter(prefix="/users")


@router.post("/", response_model=UserRead)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/{user_id}", response_model=UserRead)
def read(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)


@router.get("/", response_model=list[UserRead])
def read_all(db: Session = Depends(get_db)):
    return list_users(db)
