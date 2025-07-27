"""Kelimelere ayıran basit tokenizer."""


def tokenize(text: str) -> list[str]:
    """Metni boşluklardan böler"""
    return text.split()
