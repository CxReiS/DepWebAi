"""Slack webhook ile bildirim."""

import requests


def notify(webhook: str, text: str) -> bool:
    """Mesajı Slack'e yollar"""
    try:
        requests.post(webhook, json={"text": text}, timeout=2)
        return True
    except Exception:
        return False
