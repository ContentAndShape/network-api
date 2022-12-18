from flask import Flask
from sqlalchemy.ext.asyncio import create_async_engine

from .settings import settings
from .logger import logger


def startup(app: Flask) -> None:
    logger.debug(f"Configured app with settings {settings.dict()}")
    app.config["engine"] = create_async_engine(
        settings.alchemy_db_string
    )
