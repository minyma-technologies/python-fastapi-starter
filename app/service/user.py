from app.schema.user import UserCreate, UserUpdate
from app.model import User
from app.repo import user_repo
from sqlalchemy.orm import Session
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


class UserService:
    def can_register_user(self, db: Session, payload: UserCreate) -> bool:
        # username must be unique
        if user_repo.get_by_username(db, payload.username):
            return False
        # email must be unique
        if user_repo.get_by_email(db, payload.email):
            return False
        # add additional conditions here, like access token etc.
        return True

    def register_user(self, db: Session, payload: UserCreate) -> User | None:
        if not self.can_register_user(db, payload):
            return None
        # hash password
        password_hash = pwd_context.hash(payload.password)
        # update create object with hashed password
        payload.password = password_hash

        # save user to repo and return it
        return user_repo.create(db, payload)

    def can_update_user(self, db: Session, payload: UserUpdate) -> bool:
        # email must stay unique
        if payload.email and user_repo.get_by_email(db, payload.email):
            return False
        # username must stay unique
        if payload.username and user_repo.get_by_username(db, payload.username):
            return False
        return True

    def update_user(self, db: Session, user: User, payload: UserUpdate) -> User | None:
        if not self.can_update_user(db=db, payload=payload):
            return None
        # if password change, hash the password
        if payload.password:
            payload.password = pwd_context.hash(payload.password)
        return user_repo.update(db, user, payload)


user_service = UserService()
