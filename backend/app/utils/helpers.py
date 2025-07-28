"""Yardımcı fonksiyonlar ve çeviri işlemleri."""

import json
from functools import lru_cache
from pathlib import Path

LOCALE_DIR = Path(__file__).resolve().parents[1] / "locale"


@lru_cache(maxsize=4)
def load_locale(lang: str) -> dict:
    """Belirtilen dil dosyasını okur."""
    file_path = LOCALE_DIR / f"{lang}.json"
    if file_path.exists():
        return json.loads(file_path.read_text(encoding="utf-8"))
    return {}


def get_message(key: str, lang: str = "en", **kwargs) -> str:
    """Anahtara göre çeviri döndürür."""
    data = load_locale(lang)
    for part in key.split("."):
        if isinstance(data, dict):
            data = data.get(part)
        else:
            data = None
            break
    message = data or key
    return message.format(**kwargs) if kwargs else message
