"""WebSocket API sunucusu örneği."""

import asyncio


async def send_message(msg: str) -> None:
    """Mesajı simüle olarak gönderir"""
    await asyncio.sleep(0)
    print(f"WS: {msg}")

