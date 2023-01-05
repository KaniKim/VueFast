import os
import sys
import warnings

import pytest_asyncio
from alembic import command
from alembic.config import Config
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

sys.path.insert(1, "/home/kani/VueFast/backend")

__config_path__ = "../"
__migration_path__ = "../backend/migrations/"


@pytest_asyncio.fixture(scope="session")
def apply_migrations():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    os.environ["TESTING"] = "1"
    config = Config(__config_path__)
    config.set_main_option("script_location", __migration_path__)

    command.upgrade(config=config, revision="head")
    yield
    command.downgrade(config=config, revision="base")


@pytest_asyncio.fixture
def app(apply_migrations: None) -> FastAPI:
    from main import app

    return app


@pytest_asyncio.fixture
def engine(app: FastAPI) -> AsyncEngine:
    return app.state._db


@pytest_asyncio.fixture
async def session(engine: AsyncEngine) -> AsyncSession:
    session = AsyncSession(engine, autoflush=False, autocommit=False)
    try:
        return session
    finally:
        await session.close()


@pytest_asyncio.fixture
async def client(app: FastAPI) -> AsyncClient:

    async with AsyncClient(
        app=app,
        base_url="http://127.0.0.1:8000",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client
