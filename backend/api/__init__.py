from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=".env_fast")

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
