import functools
from packaging.version import parse as parse_version

from leak import config, parser
from leak import logger, rprint


def show_package_info(data):
    def print_row(caption_text, value):
        caption = caption_text.ljust(config.FIRST_COLUMN_LENGTH)
        print("%s %s" % (caption, value))

    info = data["info"]
    name = info["name"]
    summary = info["summary"]
    author = info["author"]
    author_email = info["author_email"]
    url = info["home_page"]
    versions_count = len(data["releases"])

    print("=" * 80)

    rprint(f"[bold bright_white]{name}[/]")
    print(summary)

    print("-" * 80)

    print_row("Author:", author)
    print_row("Author's email:", author_email)
    print_row("Available versions:", versions_count)
    print_row("Home page:", url)

    print("=" * 80)


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
