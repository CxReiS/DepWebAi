"""Bcrypt benzeri şifreleme örneği."""

import hashlib


def hash_password(password: str) -> str:
    """Parolayı karıştırır."""
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, hashed: str) -> bool:
    """Parola eşleşmesini kontrol eder."""
    return hash_password(password) == hashed
