"""Asenkron görev yöneticisi."""

from .celery_tasks import send_async


def queue_message(text: str) -> str:
    """Görevi kuyruğa ekler"""
    result = send_async.delay(text)
    return result.id
