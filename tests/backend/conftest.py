import sys
from pathlib import Path
import importlib
import pytest

sys.path.append(str(Path(__file__).resolve().parents[2] / 'backend'))

@pytest.fixture()
def db_module(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite:///:memory:")
    from app.core import config
    importlib.reload(config)
    from app.database import session as session_mod
    importlib.reload(session_mod)
    return session_mod

@pytest.fixture()
def db_session(db_module):
    db = db_module.SessionLocal()
    try:
        yield db
    finally:
        db.close()
