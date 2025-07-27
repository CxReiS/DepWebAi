"""Hata oranını hesaplar."""

errors = 0
requests = 0


def log_request(success: bool):
    """İstek sonucunu kaydeder"""
    global errors, requests
    requests += 1
    if not success:
        errors += 1


def get_error_rate() -> float:
    """Toplam hata oranı"""
    return errors / requests if requests else 0.0
