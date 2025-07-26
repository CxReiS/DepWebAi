"""Basit oran sınırlama yapısı."""


CALLS: dict[str, int] = {}


def check_rate(user: str, limit: int) -> bool:
    """Kullanıcının limitini kontrol eder."""
    count = CALLS.get(user, 0)
    if count >= limit:
        return False
    CALLS[user] = count + 1
    return True
