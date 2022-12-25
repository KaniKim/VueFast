from pydantic import BaseSettings
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "SQLALCHEMY_DATABASE_URL"

    class Config:
        env_file = ".env"


SQLALCHEMY_DATABASE_URL = Settings().SQLALCHEMY_DATABASE_URL
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, echo=True, pool_pre_ping=True, poolclass=NullPool
)


async def get_db():
    db = AsyncSession(bind=engine)
    try:
        yield db
    finally:
        await db.close()
