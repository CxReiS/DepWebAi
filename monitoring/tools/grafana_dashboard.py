"""Grafana panel şablonu."""


def create(title: str) -> dict:
    """Başlık içeren basit panel"""
    return {"title": title, "type": "graph"}
