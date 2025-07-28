import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "app"))

from app.utils import helpers


def test_json_roundtrip(tmp_path):
    data = {"x": 1, "y": [1, 2]}
    file = tmp_path / "data.json"
    helpers.write_json(file, data)
    assert helpers.read_json(file) == data


def test_slugify():
    assert helpers.slugify("Merhaba Dünya!") == "merhaba-d-nya"
