from functools import cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseBakingConfig(BaseSettings):
    model_config = SettingsConfigDict(frozen=True)


class DBSettings(BaseBakingConfig):
    db_hostname: str
    db_hostname: str
    db_password: str
    db_username: str
    db_name: str
    db_port: int = 5432
    db_enforce_ssl_mode: bool = True


class BakingConfig(BaseBakingConfig, DBSettings):
    is_debug: bool = False
    service_name: str = "testing-service"  # will be replaced in env var

    log_level: str = "DEBUG"

    # azure_storage_connection_string: str
    azure_cdn_storage_base_url: str = "https://images.baking.reubinoff.com"


@cache
def get_config() -> BakingConfig:
    return BakingConfig()
