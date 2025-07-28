import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import pytest
from fastapi import HTTPException
from app.services import role_service
from app.models.role import RoleCreate


def test_create_and_list_roles(db_session):
    db = db_session
    role = role_service.create_role(db, RoleCreate(name="admin"))
    assert role.name == "admin"
    roles = role_service.list_roles(db)
    assert len(roles) == 1 and roles[0].name == "admin"
    with pytest.raises(HTTPException):
        role_service.create_role(db, RoleCreate(name="admin"))
