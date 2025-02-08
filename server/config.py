from functools import cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    db_hostname: str
    db_password: str
    db_username: str
    db_name: str
    db_port: int = 5432
    db_enforce_ssl_mode: bool = True


class ServiceSettings(BaseSettings):
    service_name: str = "baking-hub"
    description: str = "Hub for great bread recipes"
    version: str = "1.0.0"


class BakingConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", frozen=True)

    service_settings: ServiceSettings = Field(default_factory=ServiceSettings)
    is_debug: bool = False

    log_level: str = "DEBUG"

    db_settings: DBSettings = Field(default_factory=DBSettings)
    # azure_storage_connection_string: str
    azure_cdn_storage_base_url: str = "https://images.baking.reubinoff.com"


@cache
def get_config() -> BakingConfig:
    return BakingConfig()
