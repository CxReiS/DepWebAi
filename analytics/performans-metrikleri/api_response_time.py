"""API yanıt sürelerini ölçer."""

import time
from contextlib import contextmanager

@contextmanager
def measure():
    """Süreyi hesaplar"""
    start = time.time()
    yield
    duration = time.time() - start
    print(f"Süre: {duration:.2f}s")
