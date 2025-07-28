import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from security.encryption import digital_signature as ds


def test_sign_verify_roundtrip():
    priv, pub = ds.generate_key_pair()
    msg = b"merhaba"
    sig = ds.sign(msg, priv)
    assert ds.verify(msg, sig, pub)


def test_verify_fail_with_wrong_message():
    priv, pub = ds.generate_key_pair()
    sig = ds.sign(b"merhaba", priv)
    assert not ds.verify(b"hata", sig, pub)
