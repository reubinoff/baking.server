from fastapi import FastAPI

from server.logger import init_logger
from server.middlewares import get_middlewares
from server.routers import health_router

init_logger()

routers = [health_router]

app = FastAPI(
    title="Baking Hub",
    description="Hub for great bread recipes",
    version="1.0.0",
    middleware=get_middlewares(),
)

for router in routers:
    app.include_router(router)
