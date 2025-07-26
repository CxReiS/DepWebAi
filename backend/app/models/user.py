"""Kullanıcı ORM modeli ve Pydantic şemaları."""

from sqlalchemy import Boolean, DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel, ConfigDict

from app.database.base import Base


class UserORM(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(128), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class UserCreate(BaseModel):
    username: str
    password: str


class UserRead(BaseModel):
    id: int
    username: str
    is_active: bool = True

    model_config = ConfigDict(from_attributes=True)


# Eski adıyla User
class User(UserRead):
    pass
