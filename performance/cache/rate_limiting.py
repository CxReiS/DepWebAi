"""Kullanıcı bazlı oran sınırlama."""

_requests: dict[str, int] = {}


def allow(user: str, limit: int) -> bool:
    """Limit aşılmadıysa True"""
    count = _requests.get(user, 0) + 1
    _requests[user] = count
    return count <= limit
