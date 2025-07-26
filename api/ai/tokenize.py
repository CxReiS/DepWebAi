"""Metni tokenlere ayıran API."""


def count_tokens(text: str) -> int:
    """Boşluk bazlı token sayısı"""
    return len(text.split())
