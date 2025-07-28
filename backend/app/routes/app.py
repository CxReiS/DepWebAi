"""Uygulama durum kontrolü endpointi."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/backend/app")
def backend_app():
    """Basit durum mesajı döndürür."""
    return {"message": "Backend app is running"}
