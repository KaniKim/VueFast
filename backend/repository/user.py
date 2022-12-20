import datetime
import uuid
from abc import ABC
from typing import List, Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from domain.user import User
from models.user import UserModel


class BaseUserRepository(ABC):
    def get_user_all(self, db: Session) -> List[User]:
        pass

    def get_user(self, email: str, db: Session) -> User:
        pass

    def create_user(
        self,
        email: str,
        hashed_password: str,
        name: str,
        db: Session,
    ):
        new_user = UserModel(
            email=email,
            name=name,
            hashed_password=hashed_password,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
        )
        db.add(new_user)
        return new_user

    def get_user_by_email(self, email: str, db: Session) -> User:
        pass


class UserRepository(BaseUserRepository):
    async def get_user_all(self, db: Session) -> Optional[List[User]]:

        query = await db.execute(select(UserModel))
        result = query.scalars().all()

        if result:
            db.close()
            return [res for res in result]
        db.close()
        return None

    async def get_user(self, email: str, db: Session) -> User:
        user_model = await db.query(UserModel).filter(UserModel.email == email).first()
        db.close()
        return User(
            name=user_model.name,
            email=user_model.email,
            hashed_password=user_model.hashed_password,
            created_at=user_model.created_at,
            updated_at=user_model.update_at,
        )

    async def create_user(
        self,
        email: str,
        hashed_password: str,
        name: str,
        db: Session,
    ):
        user_model = UserModel(
            id=uuid.uuid4(),
            email=email,
            hashed_password=hashed_password,
            name=name,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )
        db.add(user_model)
        try:
            await db.commit()
            db.close()
        except SQLAlchemyError as e:
            await db.rollback()
            raise e
        return user_model

    async def get_user_by_email(self, email: str, db: Session) -> Optional[User]:
        user_model = select(UserModel).where(email == email)
        user_model = await db.execute(user_model)
        if user_model:
            user = user_model.first()["UserModel"]
            return user
        return None
