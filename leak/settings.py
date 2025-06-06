import configparser
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)

CONFIG_FILEPATH = Path("~/.config/leak/config.ini").expanduser()
CONFIG_FILEPATH.parent.mkdir(parents=True, exist_ok=True)
DEFAULT_SECTION = "config"


class ConfigparserSettingsSource(PydanticBaseSettingsSource):
    def get_field_value(self, field, field_name: str) -> tuple[Any, str, bool]:
        NO_VALUE = (None, field_name, False)

        config_filepath = self.config.get("config_filepath")
        if not config_filepath.exists():
            return NO_VALUE
        config_parser = configparser.ConfigParser()
        config_parser.read(config_filepath)
        if DEFAULT_SECTION not in config_parser:
            return NO_VALUE
        config_field_name = field_name.lower().replace("_", "-")
        field_value = config_parser.get("config", config_field_name, fallback=None)
        return field_value, field_name, False

    def __call__(self) -> dict[str, Any]:
        d: dict[str, Any] = {}

        for field_name, field in self.settings_cls.model_fields.items():
            field_value, field_key, value_is_complex = self.get_field_value(
                field, field_name
            )
            field_value = self.prepare_field_value(
                field_name, field, field_value, value_is_complex
            )
            if field_value is not None:
                d[field_key] = field_value

        return d


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="LEAK_",
        case_sensitive=True,
        config_filepath=CONFIG_FILEPATH,
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            ConfigparserSettingsSource(settings_cls),
            env_settings,
        )

    DEBUG: bool = False
    DATE_FORMAT: str = "%Y/%m/%d %H:%M"
    EPOCH_BEGIN: datetime = datetime.fromtimestamp(0)
    SHOW_LATEST_RELEASES: int = 12
    SHOW_PAGER: int = 30
    PANEL_WIDTH: int = 70
    API_KEY: Optional[str] = None
    SHOW_DOWNLOADS: bool = True


config = Settings()
