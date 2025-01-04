from fastapi import FastAPI
from app.core.app_settings import AppSettings


def get_app_settings() -> AppSettings:
    return AppSettings()


def add_middleware(app: FastAPI) -> None:
    pass