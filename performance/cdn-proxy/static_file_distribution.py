"""CDN ile statik dosya dağıtımı."""


def cdn_url(path: str) -> str:
    """Tam CDN adresini döner"""
    return f"https://cdn.example.com/{path}"
