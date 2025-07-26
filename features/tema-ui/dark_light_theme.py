"""Karanlık ve aydınlık tema geçişi."""

CURRENT_THEME = "light"

def toggle_theme() -> str:
    """Temayı değiştirir"""
    global CURRENT_THEME
    CURRENT_THEME = "dark" if CURRENT_THEME == "light" else "light"
    return CURRENT_THEME

