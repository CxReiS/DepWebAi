"""Sohbet geçmişini yöneten basit sınıf."""


class ContextManager:
    """Mesajları hafızada tutar"""

    def __init__(self) -> None:
        self.history: list[str] = []

    def add(self, text: str) -> None:
        """Yeni mesaj ekler"""
        self.history.append(text)

    def get(self) -> list[str]:
        """Tüm mesajları döndürür"""
        return self.history
