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
def cli(package_name):
    """Shows all releases for a package and some info about it.

    PACKAGE_NAME Name of the package to fetch info about.
    """
    main.main(package_name=package_name)


if __name__ == "__main__":
    cli()
