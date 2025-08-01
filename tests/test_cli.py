from unittest.mock import patch

from leak import cli


@patch("leak.cli.main.main")
@patch("leak.cli.warning")
def test_executable_invocation(
    waring_mock,
    main_mock,
    runner,
):
    result = runner.invoke(cli.cli, ["podmena"])

    assert result.exit_code == 0

    main_mock.assert_called_once_with(package_name="podmena", showall=False)
    assert result.output == ""

    waring_mock.assert_called_once()


def test_invocation_missing_package_name(runner):
    result = runner.invoke(cli.cli)

    assert result.exit_code == 2


def test_version_invocation(runner):
    result = runner.invoke(cli.cli, ["--version"])

    assert result.exit_code == 0
    assert result.output.startswith("leak, version")


def test_help_invocation(runner):
    result = runner.invoke(cli.cli, ["--help"])

    assert result.exit_code == 0
    assert "Show this message and exit" in result.output
