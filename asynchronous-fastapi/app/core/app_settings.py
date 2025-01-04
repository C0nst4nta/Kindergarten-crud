import logging
import os
import sys
from typing import Any, Dict, List, Tuple

from loguru import logger
from pydantic import BaseSettings, PostgresDsn, validator

from app.core.logging import format_record, InterceptHandler
from app.core.tags_metadata import metadata_tags


class AppSettings(BaseSettings):
    """Settings used throughout the application."""

    # Application settings
    app_env: str = os.getenv("APP_ENV", "development")
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    openapi_tags: List[dict] = [tag.dict(by_alias=True) for tag in metadata_tags]
    allowed_hosts: List[str] = ["*"]

    title: str = os.getenv("APP_TITLE", "FastAPI App")
    version: str = os.getenv("APP_VERSION", "1.0.0")
    description: str = os.getenv("APP_DESCRIPTION", "A FastAPI application")
    api_prefix: str = "/api"

    # Database settings (aligning with Docker Compose)
    postgres_user: str = os.getenv("POSTGRES_USER", "admin")
    postgres_password: str = os.getenv("POSTGRES_PASSWORD", "admin")
    postgres_server: str = os.getenv("POSTGRES_SERVER", "db")  # Docker service name
    postgres_port: int = int(os.getenv("POSTGRES_PORT", 5432))
    postgres_db: str = os.getenv("POSTGRES_DB", "fastapi_db")

    # Logging
    logging_level: int = logging.DEBUG
    loggers: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        """FastAPI configuration kwargs."""
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
            "description": self.description,
        }

    @property
    def database_settings(self) -> Dict[str, Any]:
        """Database configuration settings."""
        return {
            "postgres_user": self.postgres_user,
            "postgres_password": self.postgres_password,
            "postgres_server": self.postgres_server,
            "postgres_port": self.postgres_port,
            "postgres_db": self.postgres_db,
        }

    @property
    def database_url(self) -> str:
        """Database connection URL."""
        # Build the database URL
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=self.postgres_user,
            password=self.postgres_password,
            host=self.postgres_server,
            port=str(self.postgres_port),
            path=f"/{self.postgres_db}",
        )

    @validator("postgres_port", pre=True)
    def validate_postgres_port(cls, value):
        """Validate the PostgreSQL port."""
        if not (1024 <= int(value) <= 65535):
            raise ValueError("Invalid port number for PostgreSQL")
        return value

    def configure_logging(self) -> None:
        """Configure logging settings."""
        logging.basicConfig()
        logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

        # Intercept everything at the root logger
        logging.root.handlers = [InterceptHandler()]
        logging.root.setLevel(self.logging_level)

        # Remove other logger handlers and propagate to root logger
        for name in logging.root.manager.loggerDict.keys():
            logging.getLogger(name).handlers = []
            logging.getLogger(name).propagate = True

        # Configure loguru
        logger.configure(
            handlers=[
                {"sink": sys.stdout, "serialize": False, "format": format_record, "colorize": True}
            ]
        )
