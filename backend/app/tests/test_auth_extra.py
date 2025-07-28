import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import pytest
from fastapi import HTTPException
from app.services import auth_service, user_service
from app.core import security
from app.models.auth import UserCreate


def test_register_user_and_duplicate(db_session):
    db = db_session
    user = auth_service.register_user(db, UserCreate(username="ahmet", password="1"))
    assert user.username == "ahmet"
    with pytest.raises(HTTPException):
        auth_service.register_user(db, UserCreate(username="ahmet", password="2"))


def test_decode_token_invalid():
    with pytest.raises(HTTPException):
        auth_service.decode_token(".invalid.")


def test_get_current_user_workflow(db_session):
    db = db_session
    user = user_service.create_user(db, UserCreate(username="veli", password="p"))
    token = security.create_access_token({"sub": str(user.id)})
    current = auth_service.get_current_user(db, token)
    assert current.id == user.id
    bad = security.create_access_token({"sub": "999"})
    with pytest.raises(HTTPException):
        auth_service.get_current_user(db, bad)
    with pytest.raises(HTTPException):
        auth_service.get_current_user(db, "badtoken")
