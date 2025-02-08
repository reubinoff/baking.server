from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = Field(description="The status of the health check", default="healthy")
