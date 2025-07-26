"""WebSocket ile kullanıcı bildirimi."""

import asyncio
import websockets


async def send(uri: str, message: str) -> None:
    """Mesajı websocket sunucusuna yollar"""
    async with websockets.connect(uri) as ws:
        await ws.send(message)
