import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import importlib
from pathlib import Path


def test_settings_reads_external_key(tmp_path, monkeypatch):
    key_file = tmp_path / "deep.key"
    key_file.write_text("external")
    monkeypatch.setenv("SECRET_KEY_FILE", str(key_file))
    from app.core import config
    importlib.reload(config)
    assert config.settings.SECRET_KEY == "external"


def test_origins_parsing(monkeypatch):
    monkeypatch.setenv("ALLOWED_ORIGINS", "a.com , b.com")
    from app.core import config
    importlib.reload(config)
    assert config.settings.origins == ["a.com", "b.com"]
