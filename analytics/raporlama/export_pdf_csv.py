"""Raporları dosyalara aktarır."""

import csv


def export_pdf(content: str, path: str):
    """PDF yerine düz metin yazar"""
    with open(path, "w") as f:
        f.write(content)


def export_csv(rows: list[dict], path: str):
    """CSV dosyası oluşturur"""
    if not rows:
        return
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
