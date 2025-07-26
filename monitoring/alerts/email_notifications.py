"""E-posta ile uyarı gönderir."""


def send_mail(to: str, message: str) -> None:
    """Gönderim bilgisini yazar"""
    print(f"Mail -> {to}: {message}")
