"""Slack uyarı webhook'u."""


def send_message(webhook: str, text: str) -> None:
    """Mesajı yazdırır"""
    print(f"Slack {webhook}: {text}")
