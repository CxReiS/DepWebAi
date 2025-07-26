"""Hata yönetimi."""

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse


def setup_errors(app: FastAPI) -> None:
    @app.exception_handler(HTTPException)
    async def http_exception_handler(_, exc: HTTPException):
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
