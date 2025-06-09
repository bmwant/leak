import configparser
from typing import Optional

import click

from leak import logger, main, settings


@click.command()
@click.version_option(
    prog_name="leak",
    package_name="leak",
)
@click.argument(
    "package_name",
    required=False,
)
@click.option(
    "-a",
    "--all",
    "showall",
    is_flag=True,
    default=False,
)
@click.option(
    "-s",
    "--set",
    "set_value",
    help="Set a configuration value",
)
@click.pass_context
def cli(
    ctx, package_name: Optional[str], showall: bool, set_value: Optional[str] = None
):
    """Shows all releases for a package and some info about it.

    PACKAGE_NAME Name of the package to fetch info about.
    """
    if package_name is not None and set_value is not None:
        raise click.UsageError(
            "You cannot have configuration set flag together with a package name."
        )

    if set_value is not None:
        logger.debug(f"Config setting invocation: {set_value}")
        set_config_value(set_value)
        return

    if package_name is None:
        raise click.MissingParameter(
            message="You must provide a package name to fetch information about.",
            ctx=ctx,
            param_type="argument",
            param_hint="PACKAGE_NAME",
        )

    main.main(package_name=package_name, showall=showall)


def set_config_value(set_value: str):
    """Set a configuration value."""
    if "=" not in set_value:
        raise click.BadParameter(f"Invalid format: '{set_value}'. Must be key=value.")

    key, value = set_value.split("=", 1)

    config_parser = configparser.ConfigParser()
    if settings.CONFIG_FILEPATH.exists():
        config_parser.read(settings.CONFIG_FILEPATH)

    if settings.DEFAULT_SECTION not in config_parser:
        config_parser[settings.DEFAULT_SECTION] = {}

    config_parser[settings.DEFAULT_SECTION][key.strip()] = value.strip()

    with open(settings.CONFIG_FILEPATH, "w") as f:
        config_parser.write(f)


if __name__ == "__main__":
    cli()
