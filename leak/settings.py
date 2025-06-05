from datetime import datetime

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="LEAK_",
        case_sensitive=True,
    )

    DEBUG: bool = False
    DATE_FORMAT: str = "%Y/%m/%d %H:%M"
    EPOCH_BEGIN: datetime = datetime.fromtimestamp(0)
    SHOW_LATEST_RELEASES: int = 12
    SHOW_PAGER: int = 30
    PANEL_WIDTH: int = 70


config = Settings()
