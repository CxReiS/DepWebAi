"""JWT yardımcıları."""

from datetime import datetime, timedelta, timezone
import jwt

from app.core.config import settings

ALGORITHM = "HS256"


def encode(payload: dict, expires_delta: timedelta | None = None) -> str:
    data = payload.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    data.update({"exp": expire})
    return jwt.encode(data, settings.SECRET_KEY, algorithm=ALGORITHM)


def decode(token: str) -> dict:
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
