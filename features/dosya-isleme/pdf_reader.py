"""PDF dosyalarını okuyan basit fonksiyon."""


def read_pdf(path: str) -> str:
    """Gerçek okuyucu yerine dosya metnini döner"""
    try:
        with open(path, "rb") as f:
            return f.read().decode(errors="ignore")
    except FileNotFoundError:
        return ""

