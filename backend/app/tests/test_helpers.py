import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import json
import pytest
from app.core import helpers


def test_load_locale_and_get_message(tmp_path, monkeypatch):
    file = tmp_path / "tr.json"
    file.write_text(json.dumps({"selam": "Merhaba"}), encoding="utf-8")
    monkeypatch.setattr(helpers, "LOCALE_DIR", tmp_path)
    helpers.load_locale.cache_clear()
    data = helpers.load_locale("tr")
    assert data == {"selam": "Merhaba"}
    assert helpers.get_message("selam", "tr") == "Merhaba"
    assert helpers.get_message("yok", "tr") == "yok"
