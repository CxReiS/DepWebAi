"""Kullanıcı kayıt işlemleri."""

users: dict[str, str] = {}

def register(username: str, password: str) -> bool:
    """Basit kullanıcı kaydı"""
    if username in users:
        return False
    users[username] = password
    return True

