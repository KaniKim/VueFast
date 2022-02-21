from pydantic import BaseSettings
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    DB_URL: str

    class Config:
        env_file = ".env"


settings = Settings()

SQLACLHEMY_DATABASE_URL = settings.DB_URL

engine = create_engine(SQLACLHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
