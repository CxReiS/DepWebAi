"""WebSocket ile gerçek zamanlı mesaj göndermek için basit fonksiyon."""

import asyncio


async def send_message(msg: str) -> None:
    """Mesajı ekrana basarak simüle eder."""
    await asyncio.sleep(0)
    print(f"WS mesaj: {msg}")
