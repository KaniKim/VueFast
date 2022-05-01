from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseSettings, BaseModel
from passlib.context import CryptContext
from ..repository.user import UserRepository


class Settings(BaseSettings):
    SECRET_KEY: str = "SECRET_KEY"
    ALGORITHM: str = "ALGORITHM"
    ACCESS_TOKEN_EXPIRE_MINUTES: str = "ACCESS_TOKEN_EXPIRE_MINUTES"

    class Config:
        env_file = ".env"


SECRET_KEY = Settings.SECRET_KEY
ALGORITHM = Settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = Settings.ACCESS_TOKEN_EXPIRE_MINUTES


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    usernmae: str | None = None


pwd_context = CryptContext(schemas=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Password:

    user_repo = UserRepository()

    def verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return pwd_context.hash(password)

    def authenticate_user(self, email: str, password: str):
        user = self.user_repo.get_user(email=email)

        if not user:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False

        return user


class Auth:
    user_repo = UserRepository()

    def create_access_token(self):