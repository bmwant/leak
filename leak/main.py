import time
import argparse
import datetime
import logging
import functools

import requests

from distutils.version import StrictVersion

from termcolor import colored

from .version_parser import versions_split


logging.basicConfig()
logger = logging.getLogger(__package__)


DATE_FORMAT = '%d/%m/%Y %H:%M'
EPOCH_BEGIN = datetime.datetime.fromtimestamp(0)
FIRST_COLUMN_LENGTH = 20


def get_latest_time_for_release(release):
    latest_time = EPOCH_BEGIN
    date_format = '%Y-%m-%dT%H:%M:%S'
    for release_record in release:
        upload_time = datetime.datetime.strptime(
            release_record['upload_time'], date_format
        )
        if upload_time > latest_time:
            latest_time = upload_time
    return latest_time


def get_max_downloads_for_release(release):
    max_downloads = 0
    for release_record in release:
        if release_record['downloads'] > max_downloads:
            max_downloads = release_record['downloads']
    return max_downloads


def show_package_info(data):
    def print_row(caption_text, value):
        caption = caption_text.ljust(FIRST_COLUMN_LENGTH)
        print('%s %s' % (caption, value))

    info = data['info']
    name = info['name']
    summary = info['summary']
    author = info['author']
    author_email = info['author_email']
    url = info['home_page']
    versions_count = len(data['releases'])

    print('='*80)

    header = colored(name, 'white')
    print(header)
    print(summary)

    print('-'*80)

    print_row('Author:', author)
    print_row('Author mail:', author_email)
    print_row('Available versions:', versions_count)
    print_row('Home page:', url)

    print('='*80)


def main(package_name=''):
    url_template = 'http://pypi.python.org/pypi/{package_name}/json'
    url = url_template.format(package_name=package_name)
    resp = requests.get(url)
    if resp.status_code != 200:
        error_text = colored('No such package "%s"' % package_name, 'red')
        print(error_text)
        return

    data = resp.json()
    releases = data['releases']
    show_package_info(data)
    most_popular_count = 0
    most_popular_release = None
    most_recent_release = None
    most_recent_date = EPOCH_BEGIN


    try:
        versions = sorted(releases.keys(), reverse=True, key=StrictVersion)
    except ValueError as e:
        logger.debug('Trying to sort versions as strings')
        splitter = functools.partial(versions_split, type_applyer=str)
        versions = sorted(releases.keys(), reverse=True, key=splitter)

    for release_num, release_data in releases.items():
        downloads_count = get_max_downloads_for_release(release_data)
        if downloads_count > most_popular_count:
            most_popular_count = downloads_count
            most_popular_release = release_num

        upload_date = get_latest_time_for_release(release_data)
        if upload_date > most_recent_date:
            most_recent_date = upload_date
            most_recent_release = release_num

    for version in versions:
        if version == most_popular_release == most_recent_release:
            text = colored('(%s) Most popular and recent. Use it' % version, 'green')
            print(text)
        elif version == most_popular_release:
            text = colored('(%s) Most popular. %s downloads' % (version, most_popular_count), 'yellow')
            print(text)
        elif version == most_recent_release:
            text = colored('(%s) Most recent. %s release date' % (version, most_recent_date.strftime(DATE_FORMAT)), 'blue')
            print(text)
        else:
            text = '(%s)' % version
            print(text)


def cli():
    parser = argparse.ArgumentParser(description='Show all releases for package and some info about it')
    parser.add_argument('package_name',
                        help='You should provide package name')
    args = parser.parse_args()
    main(package_name=args.package_name)


if __name__ == '__main__':
    cli()
