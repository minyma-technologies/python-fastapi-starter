from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
import logging
from alembic import config, command
from sqlalchemy.engine.url import make_url
from app.model.base import DeclarativeBase

engine = create_engine(settings.db_url)
logging.getLogger("default").info(f"Database connection created at {settings.db_url}")
dialect = make_url(settings.db_url).get_dialect()
# if using sqlite  run alembic migrations
if dialect.name == "postgresql":
    alembic_cfg = config.Config("alembic.ini")
    alembic_cfg.attributes["configure_logger"] = False
    command.upgrade(alembic_cfg, "head")
# else use create_all()
else:
    DeclarativeBase.metadata.create_all(bind=engine, checkfirst=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

