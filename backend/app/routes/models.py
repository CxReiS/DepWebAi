"""AI model yönetim endpointleri."""

from fastapi import APIRouter, HTTPException

from app.services.model_service import list_models as list_registered, run_inference

router = APIRouter(prefix="/models")

@router.get("/")
def list_models():
    """Kayıtlı modelleri döndürür."""
    return list_registered()


@router.post("/{model}")
def inference(model: str, data: str):
    """Veriyi seçili modelde işler."""
    try:
        return run_inference(model, data)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
