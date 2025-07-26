"""Ses dosyasını metne çeviren API örneği."""

import io


def voice_to_text(data: bytes) -> str:
    """Sahte dönüştürme"""
    with io.BytesIO(data) as _:
        return "metin"
