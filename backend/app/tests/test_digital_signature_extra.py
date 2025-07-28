import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import pytest
from security.encryption import digital_signature as ds


def test_verify_fail_with_wrong_key():
    priv1, pub1 = ds.generate_key_pair()
    priv2, pub2 = ds.generate_key_pair()
    sig = ds.sign(b"msg", priv1)
    assert not ds.verify(b"msg", sig, pub2)


def test_verify_fail_with_tampered_signature():
    priv, pub = ds.generate_key_pair()
    sig = ds.sign(b"msg", priv)
    tampered = sig[:-1] + bytes([sig[-1] ^ 0xFF])
    assert not ds.verify(b"msg", tampered, pub)


def test_sign_invalid_key():
    with pytest.raises(Exception):
        ds.sign(b"msg", b"invalid")
