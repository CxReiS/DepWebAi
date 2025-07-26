"""Ses dosyasını yazıya dönüştüren basit örnek."""

import io

def convert(audio_bytes: bytes) -> str:
    """Dış kütüphane olmadan sahte dönüştürme"""
    with io.BytesIO(audio_bytes) as _:
        return "metin"

