"""API yanıt sürelerini ölçer."""

import time


def measure(endpoint: str) -> float:
    """Süreyi hesaplayıp döner"""
    start = time.time()
    time.sleep(0)  # örnek gecikme
    duration = time.time() - start
    print(f"{endpoint}: {duration:.4f}s")
    return duration
