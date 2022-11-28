import secrets
from pydantic import PostgresDsn, BaseSettings, Field
from typing import Optional


class BaseAppConfig(BaseSettings):
    app_env: Optional[str] = Field(env="APP_ENV", default="dev")


class DevConfig(BaseAppConfig):
    jwt_secret: str = secrets.token_urlsafe(256)
    app_title: Optional[str] = "Minyma Python+FastAPI Template"
    db_url: PostgresDsn
    log_level: Optional[str] = "DEBUG"

    class Config:
        env_file = ".env"


class ProdConfig(BaseAppConfig):
    jwt_secret: str = secrets.token_urlsafe(256)
    app_title: Optional[str] = "Minyma Python+FastAPI Template"
    db_url: PostgresDsn
    log_level: Optional[str] = "WARN"

    class Config:
        env_file = ".env.prod"


class TestConfig(BaseAppConfig):
    jwt_secret: str = secrets.token_urlsafe(256)
    app_title: Optional[str] = "Test server"


environments = {"dev": DevConfig, "test": TestConfig, "prod": ProdConfig}
base_config = BaseAppConfig()

settings = environments[base_config.app_env]()
