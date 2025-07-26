"""Prometheus ayar dosyası üretir."""


def generate(port: int) -> str:
    """Basit yapılandırma döner"""
    return f"scrape_configs:\n- job_name: app\n  static_configs:\n  - targets: ['localhost:{port}']"
