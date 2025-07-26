"""Metinleri temizlemek için yardımcı fonksiyon."""

import re

def clean(text: str) -> str:
    """Sadece harf ve sayılar bırakır"""
    return re.sub(r"[^\w\s]", "", text)

