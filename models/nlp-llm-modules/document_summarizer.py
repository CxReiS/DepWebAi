"""Metin özetleyen basit modül."""


def summarize(text: str, limit: int = 150) -> str:
    """Kısa özet döner"""
    return text[:limit]
