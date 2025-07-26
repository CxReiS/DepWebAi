"""Oturum sürelerini hesaplar."""

from time import time

sessions: dict[str, float] = {}


def start_session(user_id: str):
    """Oturumu başlatır"""
    sessions[user_id] = time()


def end_session(user_id: str) -> float:
    """Süreyi saniye cinsinden döner"""
    start = sessions.pop(user_id, None)
    if start is None:
        return 0.0
    return time() - start
