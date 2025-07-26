"""Kaynak kullanımı için basit ölçümler."""

import random


def cpu_usage() -> float:
    """Örnek CPU yüzdesi"""
    return random.random() * 100


def memory_usage() -> float:
    """Örnek bellek yüzdesi"""
    return random.random() * 100
