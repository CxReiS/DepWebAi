"""Veritabanı için günlük yedekleme."""

from datetime import datetime


def run_backup(db_url: str) -> str:
    """Yedek dosya yolunu döner"""
    filename = f"backup-{datetime.utcnow().isoformat()}.sql"
    print(f"{db_url} -> {filename}")
    return filename
