import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2] / 'backend'))

import pytest
from app.services import model_service


def test_register_and_inference(monkeypatch):
    monkeypatch.setattr(model_service, "_models", {})
    model_service.register_model("reverse", lambda x: x[::-1])
    assert model_service.list_models() == ["reverse"]
    assert model_service.run_inference("reverse", "abc") == "cba"
    with pytest.raises(ValueError):
        model_service.run_inference("none", "x")
