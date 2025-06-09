import functools

from packaging.version import parse as parse_version
from rich import box
from rich.console import Group
from rich.highlighter import RegexHighlighter, ReprHighlighter
from rich.padding import Padding
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from leak import config, logger, parser, rprint


class SomeEmailsHighlighter(RegexHighlighter):
    """Apply style to the emails matching this simple regex"""

    base_style = "repr."
    highlights = [r"(?P<path>[\w\.\+-]+@([\w-]+\.)+[\w-]+)"]


def show_package_info(data):
    info = data["info"]
    name = info["name"]
    versions_count = len(data["releases"])

    highlight_link = ReprHighlighter()
    highlight_email = SomeEmailsHighlighter()
    table = Table(show_header=False, show_footer=False, box=box.SIMPLE, expand=True)
    table.add_row("Author:", parser.get_author(info))
    table.add_row("Email:", highlight_email(parser.get_email(info)))
    table.add_row("Home page:", highlight_link(parser.get_homepage(info)))
    table.add_row("License:", parser.get_license(info))
    table.add_row("Version:", info["version"])

    summary = Padding(Text(f"{info['summary']}", style="bold bright_white"), (1, 2))
    group = Group(
        summary,
        table,
    )
    panel = Panel(
        group,
        expand=True,
        title=f"{name}",
        subtitle=f"{versions_count} versions available",
        border_style="cyan",
        width=config.PANEL_WIDTH,
    )
    rprint(panel)


def show_package_versions(releases, downloads: dict, showall: bool = False):
    most_popular_count = 0  # noqa
    most_popular_release = None  # noqa
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
        if downloads_count:
            print(downloads_count)

        upload_date = parser.get_latest_time_for_release(release_data)
        if upload_date > most_recent_date:
            most_recent_date = upload_date
            most_recent_release = release_num  # noqa

    table = Table(
        show_header=True,
        show_footer=False,
        box=None,
        expand=True,
    )
    table.add_column(Padding("version", (1, 0)))
    table.add_column(Padding("date", (1, 0)), justify="center")
    if downloads:
        table.add_column(Padding("downloads", (1, 0)), justify="right")

    list_versions = versions if showall else versions[: config.SHOW_LATEST_RELEASES]
    for version in list_versions:
        release_data = releases[version]
        downloads_count = parser.get_downloads_for_version(
            version, downloads_data=downloads
        )
        upload_date = parser.get_latest_time_for_release(release_data)
        upload_date_str = upload_date.strftime(config.DATE_FORMAT)
        row = [version, upload_date_str]
        if downloads:
            row.append(f"{downloads_count:,}")
        table.add_row(*row)

    panel = Panel(
        table,
        expand=True,
        border_style="yellow",
        width=config.PANEL_WIDTH,
        title="List of releases" if showall else "Recent releases",
    )

    rprint(panel)


def warning(message):
    panel = Panel(
        message,
        expand=True,
        border_style="bright_red",
        width=config.PANEL_WIDTH,
        title="▲",
        title_align="left",
    )
    rprint(panel)
