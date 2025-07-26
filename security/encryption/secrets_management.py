"""Gizli verilerin yönetimi için taslak."""


SECRETS: dict[str, str] = {}


def store_secret(key: str, value: str) -> None:
    """Gizli değeri saklar."""
    SECRETS[key] = value


def get_secret(key: str) -> str:
    """Saklanan değeri döndürür."""
    return SECRETS.get(key, "")
