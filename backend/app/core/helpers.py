"""Genel yardımcı fonksiyonlar."""

from functools import lru_cache
from pathlib import Path
import json

LOCALE_DIR = Path(__file__).resolve().parents[1] / "locale"


@lru_cache(maxsize=4)
def load_locale(lang: str) -> dict:
    """Dil dosyasını yükler."""
    file_path = LOCALE_DIR / f"{lang}.json"
    if file_path.exists():
        return json.loads(file_path.read_text(encoding="utf-8"))
    return {}


def get_message(key: str, lang: str = "en", **kwargs) -> str:
    """Anahtar ile mesaj döndürür."""
    data = load_locale(lang)
    parts = key.split(".")
    for part in parts:
        if isinstance(data, dict):
            data = data.get(part)
        else:
            data = None
            break
    message = data or key
    return message.format(**kwargs) if kwargs else message
