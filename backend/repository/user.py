import datetime
import uuid
from abc import ABC
from typing import List, Optional

from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from models.user import UserModel
from domain.user import User


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
        pass

    def get_user_by_email(self, email: str, db: Session) -> User:
        pass


class UserRepository(BaseUserRepository):
    async def get_user_all(self, db: Session) -> List[User]:

        query = await db.execute(select(UserModel))
        result = query.scalars().all()

        if result:
            return [res for res in result]

        return None
    async def get_user(self, email: str, db: Session) -> User:
        user_model = await db.query(UserModel).filter(UserModel.email == email).first()
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

        try:
            db.add(user_model)
            await db.flush()
        except SQLAlchemyError as e:
            return e

    async def get_user_by_email(self, email: str, db: Session) -> Optional[User]:
        user_model = await db.execute(
            text(
                f"""
            SELECT email, name, created_at, updated_at, hashed_password
            FROM "users"
            WHERE email='{email}'; 
            """
            )
        )

        if user_model:
            user = user_model.first()
            return User(
                name=user[1],
                email=user[0],
                hashed_password=user[4],
                created_at=user[2],
                updated_at=user[3],
            )
        return None
