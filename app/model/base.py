from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy import DateTime, String, Column
from sqlalchemy.sql import func
from cuid2 import CUID

DeclarativeBase: DeclarativeMeta = declarative_base()


class BaseModel(DeclarativeBase):
    __abstract__ = True
    id = Column(String, default=CUID().generate, primary_key=True)
    date_created = Column(DateTime, default=func.now())
    date_updated = Column(DateTime, default=func.now(), onupdate=func.now())
