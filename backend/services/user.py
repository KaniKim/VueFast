from repository.user import UserRepository
from services.security import Password

from sqlalchemy.orm import Session


class UserService:
    user_repo = UserRepository()
    password_service = Password()

    async def create_user(self, password: str, email: str, name: str, db: Session):
        query_result = await self.user_repo.get_user(email=email, db=db)

        if query_result:
            return None
        hashed_password = self.password_service.get_password_hash(password=password)
        result = self.user_repo.create_user(
            email=email,
            hashed_password=hashed_password,
            name=name,
            db=db,
        )

        return result

    async def get_user_existed_or_not(self, email: str, db: Session):
        query_result = await self.user_repo.get_user_by_email(email=email, db=db)

        if not query_result:
            return False
        return True

    async def check_login_user(self, email: str, db: Session):
        result = await self.user_repo.get_user(email=email, db=db)

        if result:
            if password_service.get_password_hash(password=result.password):
                return True
            return False
        return None
