from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "SQLALCHEMY_DATABASE_URL"
    model_config = SettingsConfigDict(env_file=".env_fast")


SQLALCHEMY_DATABASE_URL = Settings().SQLALCHEMY_DATABASE_URL
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = async_sessionmaker(engine)

Base = declarative_base()
