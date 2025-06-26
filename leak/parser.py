from datetime import datetime
from email.header import decode_header
from email.utils import parseaddr
from typing import Optional

from leak import config, logger


def versions_split(version_str, type_applyer=int) -> list[int]:
    dots_count = version_str.count(".")
    if dots_count == 0:
        major, minor, patch = version_str, 0, 0
    elif dots_count == 1:
        major, minor = version_str.split(".")
        patch = 0
    elif dots_count == 2:
        major, minor, patch = version_str.split(".")
    else:
        logger.debug(
            'Incorrect version "{version}". Move to bottom when sorting'.format(
                version=version_str
            )
        )
        major, minor, patch = 0, 0, 0

    return list(map(type_applyer, (major, minor, patch)))


def get_max_downloads_for_release(release: list[dict]) -> int:
    max_downloads = 0
    for release_record in release:
        if release_record["downloads"] > max_downloads:
            max_downloads = release_record["downloads"]
    return max_downloads


def get_latest_time_for_release(release: list[dict]) -> datetime:
    latest_time = config.EPOCH_BEGIN
    date_format = "%Y-%m-%dT%H:%M:%S"
    for release_record in release:
        upload_time = datetime.strptime(release_record["upload_time"], date_format)
        if upload_time > latest_time:
            latest_time = upload_time
    return latest_time


def get_downloads_for_version(version: str, downloads_data: dict) -> int:
    downloads = 0
    for date, data in downloads_data.items():
        downloads += data.get(version, 0)
    return downloads


def decode_name(encoded_data) -> str:
    decoded_parts = decode_header(encoded_data)
    name, encoding = decoded_parts[0]
    return name.decode(encoding) if isinstance(name, bytes) else name


def get_author(info: dict) -> str:
    if "author" in info and info["author"]:
        return info["author"]

    if "author_email" in info and info["author_email"]:
        emails = info["author_email"].split(",")
        return decode_name(parseaddr(emails[0])[0])

    if "maintainer" in info and info["maintainer"]:
        return info["maintainer"]

    if "maintainer_email" in info and info["maintainer_email"]:
        emails = info["maintainer_email"].split(",")
        return decode_name(parseaddr(emails[0])[0])
    return "n/a"


def get_email(info) -> str:
    if "author_email" in info and info["author_email"]:
        emails = info["author_email"].split(",")
        return parseaddr(emails[0])[1]

    if "maintainer_email" in info and info["maintainer_email"]:
        emails = info["maintainer_email"].split(",")
        return parseaddr(emails[0])[1]
    return "n/a"


def get_homepage(info) -> str:
    if "home_page" in info and info["home_page"]:
        return info["home_page"]
    if "project_url" in info and info["project_url"]:
        return info["project_url"]
    homepage = info.get("project_urls", {}).get("Homepage", "n/a")
    return homepage


def get_license(info) -> str:
    if "license" in info and info["license"]:
        # Return the first non-empty line of the license
        # as license field can contain full license text
        return next(filter(bool, map(str.strip, info["license"].splitlines())))
    if "license_expression" in info and info["license_expression"]:
        return info["license_expression"]
    license_class = get_license_from_classifiers(info.get("classifiers", []))
    return license_class or "n/a"


def get_license_from_classifiers(classifiers: list[str]) -> Optional[str]:
    for classifier in classifiers:
        if classifier.startswith("License"):
            return classifier.split("::")[-1].strip()
