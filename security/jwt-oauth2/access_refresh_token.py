"""Erişim ve yenileme token işlemleri."""


def create_tokens(user_id: str) -> dict[str, str]:
    """Basit token sözlüğü döndürür."""
    return {"access": f"token-{user_id}", "refresh": f"refresh-{user_id}"}


def validate_token(token: str) -> bool:
    """Tokeni geçerli kabul eder."""
    return bool(token)
