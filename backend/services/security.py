import datetime

from dto.auth import TokenData
from repository.user import UserRepository

from fastapi import HTTPException, status
from pydantic import BaseSettings
from passlib.context import CryptContext
from jose import JWTError, jwt
from sqlalchemy.orm import Session


class Settings(BaseSettings):
    SECRET_KEY: str = "SECRET_KEY"
    ALGORITHM: str = "ALGORITHM"
    ACCESS_TOKEN_EXPIRE_MINUTES: str = "ACCESS_TOKEN_EXPIRE_MINUTES"
    REFRESH_TOKEN_EXPIRE_MINUTES: str = "REFRESH_TOKEN_EXPIRE_MINUTES"

    class Config:
        env_file = ".env"


class Password:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password: str, hashed_password: str):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str):
        return self.pwd_context.hash(password)


class Auth:
    user_repo = UserRepository()

    SECRET_KEY = Settings().SECRET_KEY
    ALGORITHM = Settings().ALGORITHM
    ACCESS_TOKEN_EXPIRE_MINUTES = int(Settings().ACCESS_TOKEN_EXPIRE_MINUTES)
    REFRESH_TOKEN_EXPIRE_MINUTES = int(Settings().REFRESH_TOKEN_EXPIRE_MINUTES)

    async def create_token(
        self,
        db: Session,
        data: dict,
        token_value: str = "access",
    ):
        to_encode = data.copy()

        if token_value == "access":
            expire = datetime.datetime.utcnow() + datetime.timedelta(
                minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES
            )
            to_encode.update({"exp": expire})
            encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        else:
            expire = datetime.datetime.utcnow() + datetime.timedelta(
                minutes=self.REFRESH_TOKEN_EXPIRE_MINUTES
            )
            to_encode.update({"exp": expire})
            encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
            await self.user_repo.save_refresh_token(email=data["email"], token=encoded_jwt, db=db)

        return encoded_jwt

    async def get_current_user(self, token: str, db: Session):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            username: str = payload.get("sub")

            if username is None:
                raise credentials_exception
            token_data = TokenData(usernmae=username)

        except JWTError:
            raise credentials_exception

        user = self.user_repo.get_user_by_email(email=token_data.username, db=db)

        if not user:
            return None
        return user
