import sys
from contextlib import contextmanager

import requests

from leak import config, console, logger, ui


@contextmanager
def dummy_context(*args, **kwargs):
    yield


def get_package_data(package_name: str) -> dict:
    url = f"https://pypi.org/pypi/{package_name}/json"
    resp = requests.get(url)
    if resp.status_code != 200:
        raise ValueError("No such package")

    data = resp.json()
    return data


def get_downloads_data(package_name: str) -> dict:
    if not config.API_KEY or not config.SHOW_DOWNLOADS:
        logger.warning("Skipping downloads data retrieval")
        return {}

    url = f"https://api.pepy.tech/api/v2/projects/{package_name}"
    headers = {
        "X-API-Key": config.API_KEY,
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        logger.error(f"Cannot get downloads data: [{resp.status_code}] {resp.text}")
        return {}

    data = resp.json()
    return data.get("downloads", {})


def parse_packages_from_html(html_content):
    return ""


def search_for_package(package_name: str):
    url = f"https://pypi.python.org/pypi?:action=search&term={package_name}"
    resp = requests.get(url)
    if resp.status_code != 200:
        return []
    return parse_packages_from_html(resp.text)


def main(package_name: str = "", showall: bool = False):
    try:
        package_data = get_package_data(package_name)
    except ValueError as e:
        logger.error(e)
        console.print(f"No such package [bold red]{package_name}[/].")
        return sys.exit(1)

    releases = package_data["releases"]
    downloads = get_downloads_data(package_name)
    context = dummy_context
    if showall and len(releases) > config.SHOW_PAGER:
        context = console.pager

    with context(styles=True):
        ui.show_package_info(package_data)
        ui.show_package_versions(releases, downloads, showall)
