"""Servisin durumunu kontrol eden endpoint."""


def health_check() -> dict:
    """Basit durum dönüşü"""
    return {"status": "ok"}
