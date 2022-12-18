from flask import Flask
from sqlalchemy.ext.asyncio import create_async_engine

from .settings import _settings


def startup(app: Flask) -> None:
    app.config.update(**_settings.dict())
    app.config["engine"] = create_async_engine(
        _settings.db_conn_str
    )
