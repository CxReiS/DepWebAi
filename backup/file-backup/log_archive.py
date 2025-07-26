"""Log dosyalarını arşivler."""

from pathlib import Path


def archive(log_path: str) -> str:
    """Arşiv dosya adını döner"""
    archive_file = Path(log_path).with_suffix(".tar.gz")
    print(f"Arşiv: {archive_file}")
    return str(archive_file)
