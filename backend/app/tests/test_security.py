import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from app.core import security
from app.services import auth_service


def test_password_hash_and_verify():
    plain = "sifre"
    hashed = security.get_password_hash(plain)
    assert isinstance(hashed, str) and hashed != plain
    assert security.verify_password(plain, hashed)
    assert not security.verify_password("yanlis", hashed)


def test_create_and_decode_token():
    token = security.create_access_token({"sub": "42"})
    data = auth_service.decode_token(token)
    assert data.sub == "42"


def test_generate_secret_key_unique():
    key1 = security.generate_secret_key()
    key2 = security.generate_secret_key()
    assert isinstance(key1, str) and isinstance(key2, str)
    assert key1 != key2
