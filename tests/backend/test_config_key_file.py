import importlib
import os
from pathlib import Path


def test_settings_reads_external_key(tmp_path, monkeypatch):
    key_file = tmp_path / "deepseek.key"
    key_file.write_text("external-secret")
    monkeypatch.setenv("SECRET_KEY_FILE", str(key_file))
    from app.core import config
    importlib.reload(config)
    assert config.settings.SECRET_KEY == "external-secret"
