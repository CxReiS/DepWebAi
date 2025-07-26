"""Frontend'den backend'e gelen isteğin işlenmesi."""

from typing import Any, Dict


def handle_request(payload: Dict[str, Any]) -> Dict[str, Any]:
    """İstek verisini basitçe döndürür."""
    return {"alindi": payload}
