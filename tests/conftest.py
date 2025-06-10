import pytest
from click.testing import CliRunner

from leak import settings


@pytest.fixture
def runner():
    cli_runner = CliRunner()
    yield cli_runner


@pytest.fixture(autouse=True)
def patch_settings(monkeypatch):
    monkeypatch.setattr(settings.config, "API_KEY", "")
    monkeypatch.setattr(settings.config, "SHOW_DOWNLOADS", True)
