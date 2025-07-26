"""AI cevabını kaydeden basit yapı."""

DB: list[str] = []


def save_response(answer: str) -> None:
    """Cevabı sahte veritabanına ekler."""
    DB.append(answer)
