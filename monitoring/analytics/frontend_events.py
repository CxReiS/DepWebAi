"""Ön yüz etkileşimlerini izler."""

EVENTS = []


def track_event(event: str) -> None:
    """Ekrana yazdırıp saklar"""
    EVENTS.append(event)
    print(f"Event: {event}")
