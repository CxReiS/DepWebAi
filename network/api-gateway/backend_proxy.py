"""Backend servisleri için istekleri yönlendiren proxy."""


def route_request(endpoint: str) -> str:
    """Hedef endpoint'i döner"""
    return f"Routing to {endpoint}"

