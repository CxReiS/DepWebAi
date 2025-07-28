"""AI model servisleri."""

from collections.abc import Callable

_models: dict[str, Callable[[str], str]] = {}


def register_model(name: str, handler: Callable[[str], str]) -> None:
    """Modeli kaydeder."""
    _models[name] = handler


def list_models() -> list[str]:
    """Mevcut modelleri döndürür."""
    return list(_models.keys())


def run_inference(model: str, data: str) -> str:
    """Model ile çıkarım yapar."""
    if model not in _models:
        raise ValueError("Model bulunamadı")
    return _models[model](data)


# Varsayılan örnek model
register_model("default", lambda x: x.upper())
