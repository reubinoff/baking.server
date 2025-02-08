from fastapi import FastAPI

from server.config import get_config
from server.logger import init_logger
from server.middlewares import get_middlewares
from server.routers import health_router

init_logger()

routers = [health_router]

app = FastAPI(
    title=get_config().service_settings.service_name,
    description=get_config().service_settings.description,
    version=get_config().service_settings.version,
    middleware=get_middlewares(),
)

for router in routers:
    app.include_router(router)
