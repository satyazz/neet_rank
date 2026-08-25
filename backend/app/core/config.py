from enum import StrEnum

from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(StrEnum):
    """Supported NTS runtime environments."""
    DEVELOPMENT = "development",
    TESTING = "testing",
    STAGING = "staging",
    PRODUCTION = "production"

class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""
    app_name: str = "NTS — NEET Rank System"
    app_version: str = "0.1.0"
    environment: Environment = Environment.DEVELOPMENT
    debug: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )