from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends, status
from jose import JWTError, jwt
from app.repo import user_repo
from app.config import settings
from app.api.middleware.db_session import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credantials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
        user_id = payload.get("sub")
        if user_id is None:
            credantials_exception
    except JWTError:
        raise credantials_exception
    user = user_repo.get(db, user_id)
    if not user:
        raise credantials_exception
    return user
