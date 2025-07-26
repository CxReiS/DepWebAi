"""Kullanıcı ziyaret sayısını takip eder."""

visit_data: dict[str, int] = {}


def increment(user_id: str) -> int:
    """Ziyaret sayısını artırır"""
    visit_data[user_id] = visit_data.get(user_id, 0) + 1
    return visit_data[user_id]


def get_count(user_id: str) -> int:
    """Toplam ziyaret sayısını döner"""
    return visit_data.get(user_id, 0)
