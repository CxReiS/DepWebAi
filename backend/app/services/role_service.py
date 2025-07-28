"""Rol yönetim servisleri."""

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.role import RoleCreate, RoleORM, RoleRead


def create_role(db: Session, data: RoleCreate) -> RoleRead:
    if db.query(RoleORM).filter_by(name=data.name).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Rol mevcut")
    role = RoleORM(name=data.name)
    db.add(role)
    db.commit()
    db.refresh(role)
    return RoleRead.model_validate(role)


def list_roles(db: Session) -> list[RoleRead]:
    return [RoleRead.model_validate(r) for r in db.query(RoleORM).all()]
