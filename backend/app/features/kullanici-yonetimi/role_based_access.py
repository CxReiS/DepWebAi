"""Rol kontrolü."""

roles: dict[str, list[str]] = {}


def assign(username: str, role: str) -> None:
    roles.setdefault(username, []).append(role)


def check(username: str, role: str) -> bool:
    return role in roles.get(username, [])
