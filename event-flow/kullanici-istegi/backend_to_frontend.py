"""Backend'in frontend'e ilettiği cevap."""


def build_response(data: str) -> dict:
    """Gönderilecek basit yapı."""
    return {"mesaj": data}
