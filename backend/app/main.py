"""FastAPI uygulama girişi."""

from datetime import datetime, timezone
from fastapi import Depends, FastAPI, Query, Request

from app.routes.auth import router as auth_router
from app.routes.users import router as users_router
from app.routes.models import router as models_router
from app.routes import app as app_routes
from app.utils.helpers import get_message

from app.core.cors_control import setup_cors
from app.core.error_handler import setup_errors
from app.core.rate_limiting import check_rate_limit
from app.core.logger import logger

app = FastAPI(title="DeepWebAi", dependencies=[Depends(check_rate_limit)])
setup_cors(app)
setup_errors(app)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    logger.info(
        "%s %s %s %s",
        datetime.now(timezone.utc).isoformat(),
        request.method,
        request.url.path,
        response.status_code,
    )
    return response


# Sağlık kontrolü için basit endpoint
@app.get("/health")
def health_check(lang: str = Query("en", description="Dil kodu")):
    """Servisin calisip calismadigini kontrol eder."""
    return {"status": get_message("common.health_ok", lang)}


# Router'ları ekliyoruz
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(models_router)
app.include_router(app_routes.router)
