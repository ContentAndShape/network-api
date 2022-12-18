from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    debug: bool = Field(..., env="DEBUG")
    db_name: str = Field(..., env="DB_NAME")
    db_user: str = Field(..., env="DB_USER")
    db_pass: str = Field(..., env="DB_PASS")

    @property
    def alchemy_db_string(self): 
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@localhost:5432/{self.db_name}"

    @property
    def db_string(self): 
        return f"postgresql://{self.db_user}:{self.db_pass}@localhost:5432/{self.db_name}"

    class Config:
        env_file = ".env"


settings = Settings()
