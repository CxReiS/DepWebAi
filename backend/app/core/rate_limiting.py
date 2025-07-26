"""Basit istek sınırlandırma."""

from time import time
from fastapi import Request, HTTPException, status

REQUEST_LIMIT = 10
WINDOW_SECONDS = 60

visits: dict[str, list[float]] = {}


def check_rate_limit(request: Request) -> None:
    ip = request.client.host
    now = time()
    visits.setdefault(ip, []).append(now)
    visits[ip] = [t for t in visits[ip] if now - t <= WINDOW_SECONDS]
    if len(visits[ip]) > REQUEST_LIMIT:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Limit aşıldı")
