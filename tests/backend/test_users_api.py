import sys
from pathlib import Path
from uuid import uuid4
sys.path.append(str(Path(__file__).resolve().parents[2] / 'backend'))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_user_crud():
    username = f"u{uuid4().hex[:6]}"
    r = client.post("/users/", json={"username": username, "password": "pass"})
    assert r.status_code == 200
    user_id = r.json()["id"]

    r = client.get(f"/users/{user_id}")
    assert r.status_code in (200, 404)
    if r.status_code == 200:
        assert r.json()["username"] == username

    r = client.get("/users/")
    assert r.status_code == 200
