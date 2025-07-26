"""Metin özetleyen basit API."""


def summarize(text: str, limit: int = 100) -> str:
    """Karakter sınırlı özet"""
    return text[:limit]
