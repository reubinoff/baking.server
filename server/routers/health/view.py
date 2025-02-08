import logging

from fastapi import APIRouter

from server.routers.health.models import HealthResponse

LOGGER = logging.getLogger("health")


health_router = APIRouter(prefix="/health", tags=["health"])


@health_router.get("/", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return HealthResponse(status="healthy")
