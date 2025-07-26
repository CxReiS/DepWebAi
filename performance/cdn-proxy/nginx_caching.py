"""Nginx önbellek ayar örneği."""


def cache_header(seconds: int) -> dict:
    """Cache-Control başlığı oluşturur"""
    return {"Cache-Control": f"max-age={seconds}"}
