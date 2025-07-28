import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import pytest
from fastapi import HTTPException
from starlette.requests import Request
from app.core import rate_limiting


def make_request(ip: str) -> Request:
    return Request({"type": "http", "client": (ip, 0)})


def test_rate_limit(monkeypatch):
    rate_limiting.visits.clear()
    req = make_request("1.1.1.1")
    for _ in range(rate_limiting.REQUEST_LIMIT):
        rate_limiting.check_rate_limit(req)
    with pytest.raises(HTTPException):
        rate_limiting.check_rate_limit(req)
