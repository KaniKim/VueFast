import datetime
import uuid
from abc import ABC

from sqlalchemy.orm import Session
from sqlalchemy import text

from models.user import UserModel
from domain.user import User


class BaseUserRepository(ABC):
    def get_user_all(self, db: Session) -> User:
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

    def get_user_by_id(self, id: str, db: Session) -> User:
        pass


class UserRepository(BaseUserRepository):
    async def get_user_all(self, db: Session) -> User:

        result = db.execute(
            text(
                """
            SELECT id, email, hashed_password, name, created_at, updated_at
            FROM "User";
            """
            )
        )

        if result:
            return [res for res in result.fetchall()]

    async def get_user(self, email: str, db: Session) -> User:
        user_model = db.query(UserModel).filter(UserModel.email == email).first()
        return User(
            name=user_model.name,
            nickname=user_model.nick_name,
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
        result = db.execute(
            f"""
                INSERT INTO "User" (id, email, hashed_password, name, created_at, updated_at)
                VALUES ('{user_model.id}', '{user_model.email}', '{user_model.hashed_password}', '{user_model.name}', '{user_model.created_at}', '{user_model.updated_at}');
                COMMIT;                
            """
        )

        print(result.fetchall())

    async def get_user_by_id(self, id: str, db: Session) -> User:
        user_model = db.execute(
            text(
                f"""
            SELECT email, name, created_at, updated_at
            FROM "User"
            WHERE id='{id}'; 
            """
            )
        ).first()

        return User(
            name=user_model.name,
            email=user_model.email,
            created_at=user_model.created_at.isoformat(),
            updated_at=user_model.updated_at.isoformat(),
        )
