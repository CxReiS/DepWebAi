"""Sürümlü veritabanı yedeği."""

_versions: list[str] = []


def create_version(data: str) -> int:
    """Yeni sürüm numarasını döner"""
    _versions.append(data)
    return len(_versions)
