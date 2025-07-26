"""SQLAlchemy ile basit veritabanı bağlantısı."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_session(db_url: str):
    """Verilen URL için oturum döner"""
    engine = create_engine(db_url)
    return sessionmaker(bind=engine)()

