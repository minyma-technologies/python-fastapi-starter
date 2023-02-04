from app.model.base import BaseModel
from sqlalchemy import Column, String


class User(BaseModel):
    __tablename__ = "users"
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
