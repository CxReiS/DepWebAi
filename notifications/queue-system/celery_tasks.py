"""Celery tabanlı görevler."""

from celery import Celery

app = Celery("notify", broker="redis://localhost/0")


@app.task
def send_async(message: str) -> str:
    """Mesajı işler"""
    return f"sent:{message}"
