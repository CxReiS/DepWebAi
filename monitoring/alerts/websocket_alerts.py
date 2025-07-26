"""WebSocket üzerinden uyarı yollar."""


def push(channel: str, data: str) -> None:
    """Mesajı yayınlar"""
    print(f"WS {channel}: {data}")
