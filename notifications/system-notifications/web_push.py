"""Web push bildirim gönderimi."""

import requests


def push(url: str, data: dict) -> bool:
    """Veriyi push servisine yollar"""
    try:
        requests.post(url, json=data, timeout=2)
        return True
    except Exception:
        return False
