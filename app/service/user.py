from app.schema.user import UserCreate, UserUpdate
from app.model import User
from app.repo import user_repo
from sqlalchemy.orm import Session
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


class UserService:
    def can_register_user(self, db: Session, payload: UserCreate):
        if user_repo.get_by_username(db, payload.username) or user_repo.get_by_email(
            db, payload.email
        ):
            return False
        return True

    def register_user(self, db: Session, payload: UserCreate):
        if not self.can_register_user(db, payload):
            return None
        # hash password

        password_hash = pwd_context.hash(payload.password)
        # update create object with hashed password
        create_data = payload.dict()
        create_data.update({"password": password_hash})
        new_user = User(**create_data)

        # save user to repo and return it
        return user_repo.create(db, new_user)

    def update_user(self, db: Session, user: User, payload: UserUpdate):
        if not user:
            return None
        if payload.email and user_repo.get_by_email(db, payload.email):
            return None
        if payload.username and user_repo.get_by_username(db, payload.username):
            return None
        if payload.password:
            payload.password = pwd_context.hash(payload.password)
        return user_repo.update(db, user, payload)


user_service = UserService()
