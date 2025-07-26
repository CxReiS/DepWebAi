"""AI model yönetim endpointleri."""

from fastapi import APIRouter

router = APIRouter()

@router.get("/models")
def list_models():
    """Model listesini döndürür (örnek)."""
    return ["model1", "model2"]
