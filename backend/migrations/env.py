import os
from logging.config import fileConfig

from pydantic import BaseSettings
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy import pool
from alembic import context
from sqlalchemy.exc import DatabaseError
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

load_dotenv()

section = config.config_ini_section
config.set_section_option(section, "DB_USER", os.environ.get("DB_USER"))
config.set_section_option(section, "DB_PASSWORD", os.environ.get("DB_PASSWORD"))

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

# other values from the config, defined by the needs of .env,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


class Settings(BaseSettings):
    SQLALCHEMY_TEST_DATABASE_URL: str = "SQLALCHEMY_TEST_DATABASE_URL"
    SQLALCHEMY_DATABASE_URL: str = "SQLALCHEMY_DATABASE_URL"

    class Config:
        env_file = ".env"


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """

    if os.environ.get("TESTING"):
        raise DatabaseError(
            "Running testing migrations offline currently not permitted."
        )

    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    db_url = (
        Settings().SQLALCHEMY_TEST_DATABASE_URL
        if os.environ.get("TESTING")
        else Settings().SQLALCHEMY_DATABASE_URL
    )

    if os.environ.get("TESTING"):
        default_engine = create_async_engine(db_url, isolation_level="AUTOCOMMIT")

        async with default_engine.connect() as default_conn:
            await default_conn.execute("DROP DATABASE IF EXISTS fast-test")
            await default_conn.execute("CREATE DATABASE fast-test")

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    config.set_main_option("sqlalchemy.url", db_url)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
