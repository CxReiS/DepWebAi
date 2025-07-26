"""REST API sunucusu için basit iskelet."""


def get_status() -> dict:
    """Servis durumunu döner"""
    return {"status": "ok"}

