import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "app"))

import pytest
from fastapi.testclient import TestClient
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.main import create_app
from app.core import security, rate_limiting
from app.services import auth_service, user_service
from app.models.user import UserCreate, UserORM


def test_password_hash_and_verify():
    hashed = security.get_password_hash("123")
    assert security.verify_password("123", hashed)


def test_token_create_and_decode():
    token = security.create_access_token({"sub": "7"})
    data = auth_service.decode_token(token)
    assert data.sub == "7"


def test_rate_limit(monkeypatch):
    app = create_app()
    client = TestClient(app)

    monkeypatch.setattr(rate_limiting, "REQUEST_LIMIT", 2)
    rate_limiting.visits.clear()

    assert client.get("/health").status_code == 200
    assert client.get("/health").status_code == 200
    resp = client.get("/health")
    assert resp.status_code == 429


def test_duplicate_user_transaction(db_session):
    db: Session = db_session
    user_service.create_user(db, UserCreate(username="uniq", password="1"))
    with pytest.raises(HTTPException):
        user_service.create_user(db, UserCreate(username="uniq", password="2"))
    assert db.query(UserORM).count() == 1
