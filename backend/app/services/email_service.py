"""Basit e-posta işlemleri."""

from app.core.logger import logger


def send_verification(email: str, token: str) -> None:
    logger.info("Verify %s via token %s", email, token)


def send_reset(email: str, token: str) -> None:
    logger.info("Reset password for %s via token %s", email, token)
