"""Basit bellek içi cache örneği."""

_cache: dict[str, object] = {}


def set_value(key: str, value: object) -> None:
    """Değeri saklar"""
    _cache[key] = value


def get_value(key: str) -> object | None:
    """Değeri döner"""
    return _cache.get(key)
