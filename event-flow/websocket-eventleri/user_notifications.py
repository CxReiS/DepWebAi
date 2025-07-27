"""Kullanıcı bildirimleri için basit WebSocket yapısı."""

NOTIFICATIONS: list[str] = []


def push_notification(note: str) -> None:
    """Bildirim listesine ekler."""
    NOTIFICATIONS.append(note)
