"""Uygulama ayarlarını yöneten yapı."""

from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "change-me"
    DATABASE_URL: str = "sqlite:///./app.db"
    ADMIN_USER: str = "admin"
    ADMIN_PASS: str = "password"
    ALLOWED_ORIGINS: str = "*"

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }

    @property
    def origins(self) -> list[str]:
        return [o.strip() for o in self.ALLOWED_ORIGINS.split(",") if o.strip()]


settings = Settings()
