import logging

from fastapi import APIRouter

from server.config import BakingConfig, get_config
from server.routers.health.models import HealthResponse

LOGGER = logging.getLogger("health")


health_router = APIRouter(prefix="/health", tags=["health"])


@health_router.get("/", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return HealthResponse(status="healthy")


@health_router.get("/cfg", response_model=BakingConfig)
async def get_config_check() -> BakingConfig:
    return get_config()
