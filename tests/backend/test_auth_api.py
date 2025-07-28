import sys
from pathlib import Path
from uuid import uuid4
sys.path.append(str(Path(__file__).resolve().parents[2] / 'backend'))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register_and_login():
    username = f"u{uuid4().hex[:6]}"
    r = client.post("/auth/register", json={"username": username, "password": "pass"})
    assert r.status_code == 200
    data = r.json()
    assert data["username"] == username

    r = client.post("/auth/login", json={"username": username, "password": "pass"})
    assert r.status_code == 200
    assert r.json()["access_token"]


def test_login_fail():
    r = client.post("/auth/login", json={"username": "unknown", "password": "bad"})
    assert r.status_code == 200
    assert r.json()["message"] == "Invalid username or password"
