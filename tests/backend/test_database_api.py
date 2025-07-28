import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2] / 'backend'))

from sqlalchemy import text
from app.database.session import SessionLocal


def test_session():
    db = SessionLocal()
    try:
        result = db.execute(text("SELECT 1")).scalar_one()
        assert result == 1
    finally:
        db.close()
