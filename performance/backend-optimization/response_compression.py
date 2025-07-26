"""Yanıt verisini Gzip ile sıkıştırma örneği."""

import gzip


def compress(data: bytes) -> bytes:
    """Veriyi sıkıştırıp döner"""
    return gzip.compress(data)
