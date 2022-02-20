import pytest
from click.testing import CliRunner


@pytest.fixture
def runner():
    cli_runner = CliRunner()
    yield cli_runner
