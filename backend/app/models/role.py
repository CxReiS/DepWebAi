"""Rol model tanımı."""

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel, ConfigDict

from app.database.base import Base


class RoleORM(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)


class RoleCreate(BaseModel):
    name: str


class RoleRead(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)
