
from sqlalchemy import Column, String

from models.base import BaseDBModel

Base = BaseDBModel


class User(Base):

    __tablename__ = 'users'

    email = Column(String, unique=True, nullable=False)
    username = Column(String(30), nullable=False)
    password = Column(String(156), nullable=False)
