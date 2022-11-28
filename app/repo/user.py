from app.model.user import User
from app.repo.base import CRUDBase
from app.schema.user import UserCreate, UserUpdate
from sqlalchemy.orm import Session


class UserRepo(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_username(self, db: Session, username: str) -> User:
        return db.query(User).filter(User.username == username).first()

    def get_by_email(self, db: Session, email: str) -> User:
        return db.query(User).filter(User.email == email).first()


user_repo = UserRepo(User)
