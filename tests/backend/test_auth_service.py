import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2] / 'backend'))

from app.services import auth_service
from app.core import security
from app.models.auth import LoginRequest, UserCreate
from app.models.user import UserORM


def test_authenticate_success(db_session):
    db = db_session
    user = UserORM(username="ali", hashed_password=security.get_password_hash("123"))
    db.add(user)
    db.commit()
    db.refresh(user)
    token = auth_service.authenticate(LoginRequest(username="ali", password="123"), db=db)
    data = auth_service.decode_token(token.access_token)
    assert data.sub == str(user.id)
    assert token.message == "Login successful"


def test_authenticate_fail(db_session):
    db = db_session
    user = UserORM(username="veli", hashed_password=security.get_password_hash("456"))
    db.add(user)
    db.commit()
    token = auth_service.authenticate(LoginRequest(username="veli", password="000"), db=db)
    assert token.message == "Invalid username or password"


def test_admin_auto_create(db_session, monkeypatch):
    db = db_session
    monkeypatch.setenv("ADMIN_USER", "root")
    monkeypatch.setenv("ADMIN_PASS", "secret")
    token = auth_service.authenticate(LoginRequest(username="root", password="secret"), db=db)
    created = db.query(UserORM).filter_by(username="root").first()
    assert created is not None
    data = auth_service.decode_token(token.access_token)
    assert data.sub == str(created.id)
