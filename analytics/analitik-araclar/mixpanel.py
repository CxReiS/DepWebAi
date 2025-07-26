"""Mixpanel izleme aracı."""


def track(event: str, data: dict):
    """Gösterim amaçlı veri yazdırır"""
    print(f"Mixpanel {event}: {data}")
