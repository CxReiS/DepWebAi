"""Kod bölümlerinin süresini ölçer."""

import time
from contextlib import contextmanager

@contextmanager
def measure(label: str):
    """Basit süre ölçümü"""
    start = time.time()
    yield
    duration = time.time() - start
    print(f"{label}: {duration:.2f}s")

