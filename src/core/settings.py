from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    debug: bool = Field(..., env="DEBUG")
    db_conn_str: str = Field(..., env="DB_CONN_STR")

    class Config:
        env_file = ".env"


_settings = Settings()
