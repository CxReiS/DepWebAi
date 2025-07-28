import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import pytest
from app.services import model_service


def test_register_override_and_list(monkeypatch):
    monkeypatch.setattr(model_service, "_models", {})
    model_service.register_model("test", lambda x: x.upper())
    model_service.register_model("test", lambda x: x.lower())
    assert model_service.list_models() == ["test"]
    assert model_service.run_inference("test", "Abc") == "abc"


def test_run_inference_unknown(monkeypatch):
    monkeypatch.setattr(model_service, "_models", {})
    with pytest.raises(ValueError):
        model_service.run_inference("none", "x")
