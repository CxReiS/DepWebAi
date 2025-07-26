"""Rol tabanlı erişim kontrolü taslağı."""


ROLES: dict[str, set[str]] = {
    "admin": {"read", "write"},
    "user": {"read"},
}


def has_access(role: str, action: str) -> bool:
    """Belirtilen eyleme izin var mı bakar."""
    return action in ROLES.get(role, set())
