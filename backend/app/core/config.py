"""Uygulama ayarlarını yöneten yapı."""

from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY_FILE: Path = Path(
        "D:/Python_Gereksinimleri/Venvler/secrets/deepseek.key"
    )
    SECRET_KEY: str = "dummy-secret"
    DATABASE_URL: str = "sqlite:///./app.db"
    ADMIN_USER: str = "admin"
    ADMIN_PASS: str = "password"
    ALLOWED_ORIGINS: str = "*"

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }

    def __init__(self, **values) -> None:
        super().__init__(**values)
        if self.SECRET_KEY_FILE.exists():
            self.SECRET_KEY = self.SECRET_KEY_FILE.read_text().strip()

    @property
    def origins(self) -> list[str]:
        return [o.strip() for o in self.ALLOWED_ORIGINS.split(",") if o.strip()]


settings = Settings()
