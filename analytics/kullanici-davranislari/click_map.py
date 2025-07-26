"""Sayfa tıklamalarını izler."""

clicks: dict[str, int] = {}


def log_click(area: str):
    """Belirli alan için sayacı artırır"""
    clicks[area] = clicks.get(area, 0) + 1


def get_clicks() -> dict[str, int]:
    """Toplam tıklama verisi"""
    return clicks
