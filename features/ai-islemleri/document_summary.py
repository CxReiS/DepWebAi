"""Metin özetlemek için basit fonksiyon."""


def summarize(text: str, limit: int = 100) -> str:
    """Belirtilen uzunlukta kesilmiş özet"""
    return text[:limit]

