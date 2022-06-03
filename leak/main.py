import sys

import requests

from leak import logger, rprint
from leak import ui


def get_package_data(package_name: str):
    url = f"https://pypi.org/pypi/{package_name}/json"
    resp = requests.get(url)
    if resp.status_code != 200:
        raise ValueError("No such package")

    data = resp.json()
    return data


def parse_packages_from_html(html_content):
    return ""


def search_for_package(package_name: str):
    url = f"https://pypi.python.org/pypi?:action=search&term={package_name}"
    resp = requests.get(url)
    if resp.status_code != 200:
        return []
    return parse_packages_from_html(resp.text)


def main(package_name: str = ""):
    try:
        package_data = get_package_data(package_name)
    except ValueError as e:
        logger.error(e)
        rprint(f"No such package [bold red]{package_name}[/]")
        return sys.exit(1)

    releases = package_data["releases"]
    ui.show_package_info(package_data)
    ui.show_package_versions(releases)
