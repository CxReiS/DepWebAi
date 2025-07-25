import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.services.auth_service import authenticate
from app.models.auth import LoginRequest


def test_authenticate_success():
    creds = LoginRequest(username="admin", password="password")
    token = authenticate(creds, "tr")
    assert token.access_token == "fake-token"
    assert token.message == "Giriş başarılı"


def test_authenticate_fail():
    creds = LoginRequest(username="user", password="wrong")
    token = authenticate(creds, "en")
    assert token.access_token == "invalid"
    assert token.message == "Invalid username or password"
