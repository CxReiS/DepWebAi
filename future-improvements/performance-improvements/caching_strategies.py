"""Önbellekleme stratejileri taslağı."""

CACHE: dict[str, str] = {}


def cache_data(key: str, value: str) -> None:
    """Veriyi basit önbelleğe ekler."""
    CACHE[key] = value
