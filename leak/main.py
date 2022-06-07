import sys
from contextlib import contextmanager
from typing import Dict

import requests

from leak import logger, console
from leak import config, ui


@contextmanager
def dummy_context():
    yield


def get_package_data(package_name: str):
    url = f"https://pypi.org/pypi/{package_name}/json"
    resp = requests.get(url)
    if resp.status_code != 200:
        raise ValueError("No such package")

    data = resp.json()
    return data


def get_downloads_data(package_name: str) -> Dict:
    url = f"https://api.pepy.tech/api/v2/projects/{package_name}"
    resp = requests.get(url)
    if resp.status_code != 200:
        raise RuntimeError("Cannot get downloads data for package")

    data = resp.json()
    return data["downloads"]


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
        console.print(f"No such package [bold red]{package_name}[/]")
        return sys.exit(1)

    releases = package_data["releases"]
    downloads = get_downloads_data(package_name)
    context = dummy_context
    if showall and len(releases) > config.SHOW_PAGER:
        context = console.pager

    with context():
        ui.show_package_info(package_data)
        ui.show_package_versions(releases, downloads, showall)
