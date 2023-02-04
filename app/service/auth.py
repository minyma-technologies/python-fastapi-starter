from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt

from app.schema.auth import LoginPayload
from app.repo import user_repo
from app.config import settings
from app.model import User

pwd_context = CryptContext(schemes=["bcrypt"])


class AuthService:
    def create_access_token(self, data: dict, expires_delta: timedelta | None = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.jwt_secret, algorithm="HS256")
        return encoded_jwt

    def authenticate_user(self, db: Session, payload: LoginPayload) -> User | None:
        # find user by username
        user = user_repo.get_by_username(db, payload.username)
        if user is None:
            return None
        # check password
        if not pwd_context.verify(payload.password, user.password):
            return None
        return user


auth_service = AuthService()
