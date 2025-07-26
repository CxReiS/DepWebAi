"""Oturum verilerini saklamak için basit yapı."""

_sessions: dict[str, dict] = {}


def store_session(user: str, data: dict) -> None:
    """Oturumu kaydeder"""
    _sessions[user] = data


def get_session(user: str) -> dict | None:
    """Oturumu döner"""
    return _sessions.get(user)
