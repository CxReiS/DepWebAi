"""Basit olay takip sistemi."""

subscribers: list[callable] = []


def register(func: callable):
    """Dinleyici ekler"""
    subscribers.append(func)


def emit(event: str, payload: dict):
    """Tüm dinleyicilere bildirir"""
    for func in subscribers:
        func(event, payload)
