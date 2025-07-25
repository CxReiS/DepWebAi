"""Uygulama ayarlarını yöneten yapı."""

from pathlib import Path
from pydantic import BaseSettings

class Settings(BaseSettings):
    """Temel konfigürasyon sınıfı"""

    SECRET_KEY: str = "change-me"
    DATABASE_URL: str = "sqlite:///./app.db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
