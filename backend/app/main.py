"""FastAPI uygulama girişi."""

from fastapi import Depends, FastAPI, Query
from app.routes import auth, users, models
from app.utils.helpers import get_message
from app.core.cors_control import setup_cors
from app.core.error_handler import setup_errors
from app.core.rate_limiting import check_rate_limit

app = FastAPI(title="DeepWebAi", dependencies=[Depends(check_rate_limit)])
setup_cors(app)
setup_errors(app)

# Sağlık kontrolü için basit endpoint
@app.get("/health")
def health_check(lang: str = Query("en", description="Dil kodu")):
    """Servisin çalışıp çalışmadığını kontrol eder."""
    return {"status": get_message("health_ok", lang)}

# Router'ları ekliyoruz
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(models.router, prefix="/models")
