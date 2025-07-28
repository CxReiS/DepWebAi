"""Migration yönetimi."""

from pathlib import Path
from alembic import command
from alembic.config import Config


def run_migrations(url: str) -> None:
    cfg = Config()
    cfg.set_main_option("script_location", str(Path(__file__).parent))
    cfg.set_main_option("sqlalchemy.url", url)
    command.upgrade(cfg, "head")
