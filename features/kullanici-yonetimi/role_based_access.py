"""Rol tabanlı erişim kontrolü."""

roles: dict[str, list[str]] = {}

def add_role(username: str, role: str) -> None:
    """Kullanıcıya rol atar"""
    roles.setdefault(username, []).append(role)

def has_role(username: str, role: str) -> bool:
    """Kullanıcının rolünü kontrol eder"""
    return role in roles.get(username, [])

