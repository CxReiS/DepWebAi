"""Sohbet bağlamı tutmak için basit API."""


class Context:
    """Bellekte mesaj listesi saklar"""

    def __init__(self):
        self.messages: list[str] = []

    def add(self, msg: str) -> None:
        self.messages.append(msg)

    def last(self) -> str | None:
        return self.messages[-1] if self.messages else None
