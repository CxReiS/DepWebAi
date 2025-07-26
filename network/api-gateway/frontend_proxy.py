"""Frontend isteklerini backend'e yönlendiren basit proxy."""


def forward_to_backend(path: str) -> str:
    """İstekte bulunulan yolu döner"""
    return f"Proxying {path}"

