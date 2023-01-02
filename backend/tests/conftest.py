import os
import warnings
from typing import AsyncIterator

import pytest
from alembic import command
from alembic.config import Config
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession


@pytest.fixture(scope="session")
def apply_migrations():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    os.environ["TESTING"] = "1"
    config = Config("alembic.ini")

    command.upgrade(config=config, revision="head")
    yield
    command.downgrade(config=config, revision="base")


@pytest.fixture
def app(apply_migrations: None) -> FastAPI:
    from ..main import app

    return app


@pytest.fixture
def engine(app: FastAPI) -> AsyncEngine:
    return app.state._db


@pytest.fixture
async def session(engine: AsyncEngine) -> AsyncSession:
    session = AsyncSession(engine, autoflush=False, autocommit=False)
    try:
        return session
    finally:
        await session.close()


@pytest.fixture
async def client(app: FastAPI) -> AsyncIterator[AsyncClient]:
    async with LifespanManager(app):
        async with AsyncClient(
            app=app,
            base_url="http://testserver",
            headers={"Content-Type": "application/json"},
        ) as client:
            yield client
