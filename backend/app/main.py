from fastapi import FastAPI

from app.core.config import Settings


def create_app(settings: Settings) ->FastAPI:
    return FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        debug=settings.debug,
    )

settings = Settings()
app = create_app(settings)