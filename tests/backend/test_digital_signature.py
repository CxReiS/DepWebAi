import pytest
from security.encryption import digital_signature as ds


def test_sign_verify_roundtrip():
    priv, pub = ds.generate_key_pair()
    message = b"merhaba"
    sig = ds.sign(message, priv)
    assert ds.verify(message, sig, pub)


def test_verify_fail_with_wrong_message():
    priv, pub = ds.generate_key_pair()
    message = b"merhaba"
    sig = ds.sign(message, priv)
    assert not ds.verify(b"hata", sig, pub)
