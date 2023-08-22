from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "SQLALCHEMY_DATABASE_URL"
    model_config = SettingsConfigDict(env_file=".env_fast")


SQLALCHEMY_DATABASE_URL = Settings().SQLALCHEMY_DATABASE_URL
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, echo=True, pool_pre_ping=True, poolclass=NullPool
)

Base = declarative_base()
