"""Sohbet geçmişini tutan basit yönetici."""

class ContextManager:
    """Bellekte mesaj listesi saklar"""

    def __init__(self):
        self.history: list[str] = []

    def add(self, message: str) -> None:
        """Mesajı geçmişe ekler"""
        self.history.append(message)

    def last(self) -> str | None:
        """Son mesajı döndürür"""
        return self.history[-1] if self.history else None

