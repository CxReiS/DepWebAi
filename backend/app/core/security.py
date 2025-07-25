"""Güvenlik yardımcıları."""

import os
from pathlib import Path


def load_keys():
    """'secrets' klasöründen anahtarları okur."""
    key_path = Path("secrets/secret.key")
    if key_path.exists():
        return key_path.read_text().strip()
    return os.environ.get("SECRET_KEY", "change-me")
