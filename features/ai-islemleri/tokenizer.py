"""Metni kelimelere bölen basit tokenizer."""

def tokenize(text: str) -> list[str]:
    """Boşluklara göre ayırır"""
    return text.split()

