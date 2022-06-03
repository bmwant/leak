import functools
from packaging.version import parse as parse_version

from rich import box
from rich.console import Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.padding import Padding

from leak import config, parser
from leak import logger, rprint


def show_package_info(data):
    info = data["info"]
    name = info["name"]
    author = info["author"]
    author_email = info["author_email"]
    url = info["home_page"]
    versions_count = len(data["releases"])

    table = Table(show_header=False, show_footer=False, box=box.SIMPLE)
    table.add_row("Author:", author)
    table.add_row("Email:", author_email)
    table.add_row("Home page:", url)
    summary = Padding(Text(f'{info["summary"]}', style="bold bright_white"), (1, 2))
    group = Group(
        summary,
        table,
    )
    panel = Panel(
        group,
        expand=False,
        title=f"{name}",
        subtitle=f"{versions_count} versions available",
    )
    rprint(panel)


def show_package_versions(releases):
    most_popular_count = 0
    most_popular_release = None
    most_recent_release = None
    most_recent_date = config.EPOCH_BEGIN

    try:
        versions = sorted(releases.keys(), reverse=True, key=parse_version)
    except ValueError as e:
        logger.debug(e)
        logger.debug("Trying to sort versions as strings")
        splitter = functools.partial(parser.versions_split, type_applyer=str)
        versions = sorted(releases.keys(), reverse=True, key=splitter)

    for release_num, release_data in releases.items():
        downloads_count = parser.get_max_downloads_for_release(release_data)
        if downloads_count > most_popular_count:
            most_popular_count = downloads_count
            most_popular_release = release_num

        upload_date = parser.get_latest_time_for_release(release_data)
        if upload_date > most_recent_date:
            most_recent_date = upload_date
            most_recent_release = release_num

    for version in versions:
        if version == most_popular_release == most_recent_release:
            rprint(f"[green]({version}) Most popular and recent. Use this one.[/]")
        elif version == most_popular_release:
            rprint(
                f"[yellow]({version}) Most popular: {most_popular_count} downloads.[/]"
            )
        elif version == most_recent_release:
            release_date = most_recent_date.strftime(config.DATE_FORMAT)
            rprint(f"[cyan]({version}) Most recent: {release_date} release date.[/]")
        else:
            rprint(f"({version})")
