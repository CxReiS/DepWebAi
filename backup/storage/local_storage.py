"""Yerel depolama işlemleri."""

from pathlib import Path


def save(path: str, directory: str) -> str:
    """Dosya yolunu döner"""
    target = Path(directory) / Path(path).name
    print(f"Local save {target}")
    return str(target)
