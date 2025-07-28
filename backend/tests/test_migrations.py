import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from sqlalchemy import create_engine, inspect
from app.database.migrations import run_migrations


def test_run_migrations(tmp_path):
    url = f"sqlite:///{tmp_path/'db.sqlite'}"
    run_migrations(url)
    engine = create_engine(url)
    insp = inspect(engine)
    tables = insp.get_table_names()
    assert "users" in tables and "roles" in tables
