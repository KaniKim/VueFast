import datetime

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseSettings, BaseModel
from passlib.context import CryptContext
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from repository.user import UserRepository


class Settings(BaseSettings):
    SECRET_KEY: str = "SECRET_KEY"
    ALGORITHM: str = "ALGORITHM"
    ACCESS_TOKEN_EXPIRE_MINUTES: str = "ACCESS_TOKEN_EXPIRE_MINUTES"

    class Config:
        env_file = ".env"


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class TokenData(BaseModel):
    username: str = None


class Password:

    user_repo = UserRepository()

    def verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return pwd_context.hash(password)

    async def authenticate_user(self, email: str, password: str, db: Session):
        user = await self.user_repo.get_user_by_email(email=email, db=db)
        if not user:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False

        return user


class Auth:
    user_repo = UserRepository()
    SECRET_KEY = Settings().SECRET_KEY
    ALGORITHM = Settings().ALGORITHM
    ACCESS_TOKEN_EXPIRE_MINUTES = int(Settings().ACCESS_TOKEN_EXPIRE_MINUTES)

    def create_access_token(self, data: dict, expires_delta: datetime.timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.datetime.utcnow() + expires_delta
        else:
            expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    async def get_current_user(self, token: str = Depends(oauth2_scheme)):
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

        user = self.user_repo.get_user(email=token_data.usernmae)
        if user is None:
            raise credentials_exception

        return user
