import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import pytest
from fastapi import HTTPException
from app.services import user_service
from app.models.user import UserCreate


def test_get_user_not_found(db_session):
    with pytest.raises(HTTPException):
        user_service.get_user(db_session, 999)
