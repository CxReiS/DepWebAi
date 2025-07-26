"""JWT oluşturma ve doğrulama işlemleri."""

import time
import hmac
import hashlib
import base64

SECRET = "secret"

def create_token(username: str) -> str:
    """Basit zaman damgalı token"""
    payload = f"{username}:{int(time.time())}"
    sig = hmac.new(SECRET.encode(), payload.encode(), hashlib.sha256).hexdigest()
    token = base64.urlsafe_b64encode(f"{payload}:{sig}".encode()).decode()
    return token

def verify_token(token: str) -> bool:
    """Token geçerli mi kontrol eder"""
    try:
        data = base64.urlsafe_b64decode(token).decode()
        username, ts, sig = data.split(":")
        expected = hmac.new(SECRET.encode(), f"{username}:{ts}".encode(), hashlib.sha256).hexdigest()
        return hmac.compare_digest(sig, expected)
    except Exception:
        return False

