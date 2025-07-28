import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2] / 'backend'))

import pytest
from fastapi import HTTPException
from app.services import user_service
from app.models.user import UserCreate


def test_create_and_get_user(db_session):
    db = db_session
    user = user_service.create_user(db, UserCreate(username="ali", password="123"))
    fetched = user_service.get_user(db, user.id)
    assert fetched.username == "ali"


def test_create_user_duplicate(db_session):
    db = db_session
    user_service.create_user(db, UserCreate(username="ali", password="123"))
    with pytest.raises(HTTPException):
        user_service.create_user(db, UserCreate(username="ali", password="456"))


def test_list_users(db_session):
    db = db_session
    user_service.create_user(db, UserCreate(username="a", password="1"))
    user_service.create_user(db, UserCreate(username="b", password="2"))
    users = user_service.list_users(db)
    assert len(users) == 2
