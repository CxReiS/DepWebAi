"""Uygulama giriş noktası."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Awaitable, Callable

from fastapi import Depends, FastAPI, Query, Request, Response
from routes import health
from app.core.cors_control import setup_cors
from app.core.error_handler import setup_errors
from app.core.logger import logger
from app.core.rate_limiting import check_rate_limit
from app.routes import app as app_routes
from app.routes.auth import router as auth_router
from app.routes.models import router as models_router
from app.routes.users import router as users_router
from app.utils.helpers import get_message


def create_app() -> FastAPI:
    app = FastAPI(title="DeepWebAi", dependencies=[Depends(check_rate_limit)])
    setup_cors(app)
    setup_errors(app)

    @app.middleware("http")
    async def log_requests(
        request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        response = await call_next(request)
        logger.info(
            "%s %s %s %s",
            datetime.now(timezone.utc).isoformat(),
            request.method,
            request.url.path,
            response.status_code,
        )
        return response

    @app.get("/health")
    def health_check(lang: str = Query("en", description="Dil kodu")) -> dict[str, str]:
        return {"status": get_message("common.health_ok", lang)}

    app.include_router(auth_router)
    app.include_router(users_router)
    app.include_router(models_router)
    app.include_router(app_routes.router)

    return app


app = create_app()

app.include_router(health.router)