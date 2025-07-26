"""CORS kontrolü için taslak."""


ALLOWED_ORIGINS = ["*"]


def is_allowed(origin: str) -> bool:
    """Origin izinli mi bakar."""
    return origin in ALLOWED_ORIGINS or "*" in ALLOWED_ORIGINS
