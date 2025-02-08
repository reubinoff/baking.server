from fastapi import FastAPI

from server.logger import init_logger
from server.middlewares import get_middlewares

init_logger()


app = FastAPI(
    title="Baking Hub",
    description="Hub for great bread recipes",
    version="1.0.0",
    middleware=get_middlewares(),
)


# Basic health check endpoint
@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "healthy"}
