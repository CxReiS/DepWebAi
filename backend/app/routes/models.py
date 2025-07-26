"""AI model yönetim endpointleri."""

from fastapi import APIRouter

router = APIRouter(prefix="/models")

@router.get("/")
def list_models():
    """Model listesini döndürür (örnek)."""
    return ["model1", "model2"]
