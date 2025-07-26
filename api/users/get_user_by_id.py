"""ID'ye göre kullanıcı getirir."""


def get_user_by_id(user_id: int) -> dict | None:
    """Basit kullanıcı arama"""
    users = {
        1: {"id": 1, "username": "alice"},
        2: {"id": 2, "username": "bob"},
    }
    return users.get(user_id)
