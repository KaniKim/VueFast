import datetime
import uuid
from abc import ABC

from fastapi import Depends
from sqlalchemy.orm import Session

from ..models.user import UserModel
from ..domain.user import User
from . import SessionLocal


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

    def get_user_by_id(self, id: str, db: Session = Depends(get_db)) -> User:
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
        db.execute(
            f"""
                INSERT INTO User (id, email, hashed_password, nickname, name, created_at, updated_at)
                VALUES ({user_model.id}, {user_model.email}, {user_model.hashed_password}, {user_model.nickname}, {user_model.name}, {user_model.created_at}, {user_model.updated_at});
                COMMIT;                
            """
        )

    def get_user_by_id(self, id: str, db: Session = Depends(get_db)) -> User:
        user_model = db.execute(
            f"""
            SELECT id
            FROM User
            WHERE email={id}; 
            """
        )
        return User(
            name=user_model.name,
            nickname=user_model.nick_name,
            email=user_model.email,
            hashed_password=user_model.hashed_password,
            created_at=user_model.created_at,
            updated_at=user_model.update_at,
        )
