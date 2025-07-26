"""SQLAlchemy modelleri."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    """Kullanıcı tablosu"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

class Model(Base):
    """Model bilgilerini saklar"""
    __tablename__ = "models"
    id = Column(Integer, primary_key=True)
    name = Column(String)
