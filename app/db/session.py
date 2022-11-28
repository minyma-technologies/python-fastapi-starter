from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from functools import lru_cache
from sqlalchemy.orm import sessionmaker
from app.config import settings
import logging

Base = declarative_base()

# make session singleton via lru-cache
@lru_cache(maxsize=1)
def session_factory():
    engine = create_engine(settings.db_url)
    logging.getLogger("default").info(
        f"Database connection created at {settings.db_url}"
    )
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal
