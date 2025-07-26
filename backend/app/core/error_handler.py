"""Hata yönetimi."""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app.core.logger import logger


def setup_errors(app: FastAPI) -> None:
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        logger.error("%s %s %s", request.method, request.url.path, exc.status_code)
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
