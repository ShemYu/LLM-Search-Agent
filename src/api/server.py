from fastapi import FastAPI

from src.api.endpoints import healthz, test


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(healthz.router)
    app.include_router(test.router)

    return app
