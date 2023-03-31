import datetime
import uuid
from abc import ABC
from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from dto.user import User
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
        pass

    def get_user_by_email(self, email: str, db: Session) -> User:
        pass


class UserRepository(BaseUserRepository):
    @classmethod
    def ConvertToModel(cls, user: User):
        return UserModel(
            id=user.id,
            name=user.name,
            hashed_password=user.hashed_password,
            email=user.email,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    @classmethod
    def ConvertToDTO(cls, user: UserModel):
        return User(
            id=user.id,
            name=user.name,
            password=user.hashed_password,
            email=user.email,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    async def get_user_all(self, db: Session) -> Optional[List[User]]:

        query = await db.execute(select(UserModel))
        result = query.scalars().all()

        if result:
            return [self.ConvertToDTO(res) for res in result]
        return None

    async def get_user(self, email: str, db: Session) -> Optional[User]:

        query = select(UserModel).where(UserModel.email == email)
        user_model = await db.execute(query).scalar()

        if user_model:
            return self.ConvertToDTO(user=user_model)
        return None

    async def create_user(
        self,
        email: str,
        hashed_password: str,
        name: str,
        db: Session,
    ) -> User:

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
            await db.refresh(user_model)
        except SQLAlchemyError as error:
            db.rollback()
            raise error

        return self.ConvertToDTO(user_model)

    async def get_user_by_email(self, email: str, db: Session) -> Optional[User]:
        query = await db.execute(select(UserModel).where(UserModel.email == email))
        user = query.scalars().first()
        if user:
            return self.ConvertToDTO(user)
        return None

    async def save_refresh_token(self, email: str, token: str, db: Session) -> bool:
        if await self.get_user_by_email(email=email, db=db):
            query = update(UserModel).where(UserModel.email == email)
            query = query.values(refresh_token=token).execution_options(synchronize_session="fetch")
            await db.execute(query)
            await db.commit()
            return True
        return False
