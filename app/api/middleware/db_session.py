from sqlalchemy.orm import Session
from typing import Iterator
from app.db import SessionLocal

def get_db() -> Iterator[Session]:
    db: Session = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
    finally:
        db.close()

