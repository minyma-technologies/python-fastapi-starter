from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends, status
from jose import JWTError, jwt

from app.repo import user_repo
from app.db.session import session_factory
from app.config import settings


def get_db_session():
    SessionLocal = session_factory()
    db: Session = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
    finally:
        db.close()


def get_db():
    if settings.app_env != "test":
        return get_db_session()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    credantials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
        user_id: str = payload.get("sub")
        if user_id is None:
            credantials_exception
    except JWTError:
        raise credantials_exception
    user = user_repo.get(db, user_id)
    if not user:
        raise credantials_exception
    return user
