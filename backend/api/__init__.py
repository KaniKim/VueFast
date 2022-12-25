from pydantic import BaseSettings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "SQLALCHEMY_DATABASE_URL"

    class Config:
        env_file = ".env"


SQLALCHEMY_DATABASE_URL = Settings().SQLALCHEMY_DATABASE_URL
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
