from loguru import logger
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.config import get_app_settings
from app.db.models.base import Base


def get_async_engine() -> AsyncEngine:
    """Create and return an asynchronous database engine."""
    try:
        return create_async_engine(
            get_app_settings().database_url,
            future=True,
        )
    except SQLAlchemyError as e:
        logger.error(f"Failed to create async database engine: {e}")
        raise


async def initialize_database() -> None:
    """Initialize the database by creating all tables."""
    try:
        async_engine = get_async_engine()
        async with async_engine.begin() as async_conn:
            await async_conn.run_sync(Base.metadata.create_all)
            logger.success("Database initialization successful.")
    except SQLAlchemyError as e:
        logger.error(f"Error initializing the database: {e}")
        raise


def get_sessionmaker() -> sessionmaker:
    """Return a sessionmaker for async database sessions."""
    async_engine = get_async_engine()
    return sessionmaker(
        bind=async_engine,
        expire_on_commit=False,
        class_=AsyncSession,
    )

