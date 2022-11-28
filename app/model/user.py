from app.db.session import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String
import uuid


class User(Base):
    __tablename__ = "users"
    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    )
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
