"""FastAPI uygulama girişi."""

from fastapi import FastAPI
from app.routes import auth, users

app = FastAPI(title="DeepWebAi")

# Sağlık kontrolü için basit endpoint
@app.get("/health")
def health_check():
    """Servisin çalışıp çalışmadığını kontrol eder."""
    return {"status": "ok"}

# Router'ları ekliyoruz
app.include_router(auth.router, prefix="/auth")
app.include_router(users.router, prefix="/users")
