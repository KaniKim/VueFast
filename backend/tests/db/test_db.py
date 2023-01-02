import logging

from databases import Database
from fastapi import FastAPI
from pydantic import BaseSettings

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    SQLALCHEMY_TEST_DATABASE_URL: str = "SQLALCHEMY_TEST_DATABASE_URL"

    class Config:
        env_file = ".env"


async def connect_to_db(app: FastAPI) -> None:
    db_url = Settings.SQLALCHEMY_TEST_DATABASE_URL
    database = Database(db_url, min_size=2, max_size=10)

    try:
        await database.connect()
        app.state._db = database

    except Exception as e:
        logger.warning("--- DB CONNECTION ERROR --")
        logger.warning(e)
        logger.warning("--- DB CONNECTION ERROR ---")


async def close_db_connection(app: FastAPI) -> None:
    try:
        await app.state._db.disconnect()
    except Exception as e:
        logger.warning("--- DB DISCONNECT ERROR ---")
        logger.warning(e)
        logger.warning("--- DB DISCONNECT ERROR ---")
