"""Sorgu optimizasyonu için örnek fonksiyon."""

def optimized_search(rows: list[dict], column: str, value) -> list[dict]:
    """Liste içinde hızla filtreleme yapar"""
    return [r for r in rows if r.get(column) == value]
