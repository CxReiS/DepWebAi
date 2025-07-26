"""Uygulama ayarlarını yöneten yapı."""

from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Temel konfigürasyon sınıfı"""

    SECRET_KEY: str = "change-me"
    DATABASE_URL: str = "sqlite:///./app.db"

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }

settings = Settings()
