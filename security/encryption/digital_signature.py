"""Dijital imza işlemleri."""

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature


def generate_key_pair() -> tuple[bytes, bytes]:
    """PEM formatında anahtar çifti üretir."""
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()
    pem_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    pem_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    return pem_private, pem_public


def sign(message: bytes, pem_private: bytes) -> bytes:
    """İmzayı döndürür."""
    private_key = serialization.load_pem_private_key(pem_private, password=None)
    return private_key.sign(message, ec.ECDSA(hashes.SHA256()))


def verify(message: bytes, signature: bytes, pem_public: bytes) -> bool:
    """İmzanın doğruluğunu kontrol eder."""
    public_key = serialization.load_pem_public_key(pem_public)
    try:
        public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
        return True
    except InvalidSignature:
        return False
