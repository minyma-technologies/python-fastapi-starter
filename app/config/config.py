import secrets
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    jwt_secret: str = secrets.token_urlsafe(256)
    db_url: str
    log_level: str = "DEBUG"
    app_title: str = "My app"


class EnvironmentSelector(BaseSettings):
    app_env: str = Field(..., env="APP_ENV")


dotenv_files = {"dev": "dev.env", "test": "test.env", "prod": ".prod.env"}
env_selector = EnvironmentSelector()
settings = Settings(_env_file=dotenv_files[env_selector.app_env.lower()])
