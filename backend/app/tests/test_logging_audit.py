import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "app"))

from fastapi import HTTPException
from fastapi.testclient import TestClient

from app.main import create_app
from app.services import email_service
from monitoring.logging import app_errors, audit_logs
from app.core.logger import logger


def test_email_logging(caplog):
    caplog.set_level("INFO", logger=logger.name)
    email_service.send_verification("a@test.com", "tok")
    assert any("Verify a@test.com via token tok" in r.getMessage() for r in caplog.records)
    caplog.clear()
    email_service.send_reset("a@test.com", "tok")
    assert any("Reset password for a@test.com via token tok" in r.getMessage() for r in caplog.records)


def test_app_error_log(capsys):
    app_errors.log_error("fail")
    captured = capsys.readouterr().out.strip()
    assert captured == "ERROR: fail"


def test_audit_record_action():
    audit_logs.LOGS.clear()
    audit_logs.record_action("login")
    assert audit_logs.LOGS == ["login"]


def test_error_handler_logs(caplog):
    app = create_app()

    @app.get("/err")
    def err_route():
        raise HTTPException(status_code=418, detail="teapot")

    client = TestClient(app)
    caplog.set_level("ERROR", logger=logger.name)
    response = client.get("/err")
    assert response.status_code == 418
    assert any("/err" in r.getMessage() and "418" in r.getMessage() for r in caplog.records)


def test_request_logging(caplog):
    app = create_app()
    client = TestClient(app)
    caplog.set_level("INFO", logger=logger.name)
    response = client.get("/health")
    assert response.status_code == 200
    assert any("/health" in r.getMessage() for r in caplog.records)
