"""FastAPI uygulama girişi."""

from fastapi import FastAPI, Query
from app.routes import auth, users, models
from app.utils.helpers import get_message

app = FastAPI(title="DeepWebAi")

# Sağlık kontrolü için basit endpoint
@app.get("/health")
def health_check(lang: str = Query("en", description="Dil kodu")):
    """Servisin çalışıp çalışmadığını kontrol eder."""
    return {"status": get_message("health_ok", lang)}

# Router'ları ekliyoruz
app.include_router(auth.router, prefix="/auth")
app.include_router(users.router, prefix="/users")
app.include_router(models.router, prefix="/models")
