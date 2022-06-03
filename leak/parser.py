import datetime

from leak import config, logger


def versions_split(version_str, type_applyer=int):
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
            'Incorrect version "{version}". '
            "Move to bottom when sorting".format(version=version_str)
        )
        major, minor, patch = 0, 0, 0

    return list(map(type_applyer, (major, minor, patch)))


def get_max_downloads_for_release(release):
    max_downloads = 0
    for release_record in release:
        if release_record["downloads"] > max_downloads:
            max_downloads = release_record["downloads"]
    return max_downloads


def get_latest_time_for_release(release):
    latest_time = config.EPOCH_BEGIN
    date_format = "%Y-%m-%dT%H:%M:%S"
    for release_record in release:
        upload_time = datetime.datetime.strptime(
            release_record["upload_time"], date_format
        )
        if upload_time > latest_time:
            latest_time = upload_time
    return latest_time
