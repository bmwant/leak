import click

from leak import main


@click.command()
@click.version_option(
    prog_name="leak",
    package_name="leak",
)
@click.argument(
    "package_name",
    required=True,
)
@click.option(
    "-a",
    "--all",
    "showall",
    is_flag=True,
    default=False,
)
def cli(package_name, showall):
    """Shows all releases for a package and some info about it.

    PACKAGE_NAME Name of the package to fetch info about.
    """
    main.main(package_name=package_name, showall=showall)


if __name__ == "__main__":
    cli()
