"""Kullanıcı işlem geçmişini tutar."""

LOGS = []


def record_action(action: str) -> None:
    """Eylemi listede saklar"""
    LOGS.append(action)
