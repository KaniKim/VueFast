import datetime
import uuid
from abc import ABC

from fastapi import Depends
from sqlalchemy.orm import Session

from ..models.user import UserModel
from ..domain.user import User
from . import SessionLocal, engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class BaseUserRepository(ABC):
    def get_user(self, email: str, db: Session = Depends(get_db)) -> User:
        pass

    def create_user(
        self,
        email: str,
        hashed_password: str,
        name: str,
        nickname: str,
        db: Session = Depends(get_db),
    ):
        pass


class UserRepository(BaseUserRepository):
    def get_user(self, email: str, db: Session = Depends(get_db)) -> User:
        user_model = db.query(UserModel).filter(UserModel.email == email).first()
        return User(
            name=user_model.name,
            nickname=user_model.nick_name,
            email=user_model.email,
            hashed_password=user_model.hashed_password,
            created_at=user_model.created_at,
            updated_at=user_model.update_at,
        )

    def create_user(
        self,
        email: str,
        hashed_password: str,
        name: str,
        nickname: str,
        db: Session = Depends(get_db),
    ):
        user_model = UserModel(
            id=uuid.uuid4(),
            email=email,
            hashed_password=hashed_password,
            nickname=nickname,
            name=name,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
        )
        db.add(user_model)
        db.commit()
        db.refresh()
