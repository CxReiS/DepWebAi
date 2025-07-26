"""Kullanıcı listesi döndürür."""


def get_users() -> list[dict]:
    """Örnek kullanıcıları verir"""
    return [
        {"id": 1, "username": "alice"},
        {"id": 2, "username": "bob"},
    ]
