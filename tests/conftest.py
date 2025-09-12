import json
from pathlib import Path

import pytest
from click.testing import CliRunner

from leak import settings

CURRENT_DIR = Path(__file__).parent.resolve()
DATA_DIR = CURRENT_DIR / "data"


@pytest.fixture
def runner():
    cli_runner = CliRunner()
    yield cli_runner


@pytest.fixture(autouse=True)
def patch_settings(monkeypatch):
    monkeypatch.setattr(settings.config, "API_KEY", "")
    monkeypatch.setattr(settings.config, "SHOW_DOWNLOADS", True)


@pytest.fixture
def package_data():
    def _get_package_data(package_name: str) -> dict:
        with open(DATA_DIR / f"{package_name}_package_data.json") as f:
            data = json.load(f)
        return data["info"]

    return _get_package_data


@pytest.fixture
def downloads_data():
    def _get_downloads_data(package_name: str) -> dict:
        with open(DATA_DIR / f"{package_name}_downloads_data.json") as f:
            data = json.load(f)
        return data

    return _get_downloads_data
