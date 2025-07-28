import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2] / 'backend'))

from app.models.user import User


def test_user_model():
    user = User(id=1, username="alice")
    assert user.id == 1
    assert user.username == "alice"
