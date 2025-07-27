"""HTTPS/SSL yapılandırması için örnek."""


def is_secure(url: str) -> bool:
    """URL https ile başlıyor mu diye kontrol eder."""
    return url.startswith("https://")
