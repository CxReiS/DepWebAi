"""FastAPI benzeri asenkron endpoint örnegi."""

import asyncio

async def sample_endpoint() -> dict:
    """Kısa gecikmeli yanıt döner"""
    await asyncio.sleep(0)
    return {"message": "ok"}
