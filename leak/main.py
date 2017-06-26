import datetime
import functools

import requests

from packaging.version import parse as parse_version

from termcolor import colored

from leak import logger
from leak import EPOCH_BEGIN, FIRST_COLUMN_LENGTH, DATE_FORMAT
from leak.version_parser import versions_split


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


def get_package_data(package_name):
    url_template = 'http://pypi.python.org/pypi/{package_name}/json'
    url = url_template.format(package_name=package_name)
    resp = requests.get(url)
    if resp.status_code != 200:
        raise ValueError('No such package')

    data = resp.json()
    return data


def parse_packages_from_html(html_content):
    return ''


def search_for_package(package_name):
    url_template = ('https://pypi.python.org/'
                    'pypi?:action=search&term={package_name}')
    url = url_template.format(package_name=package_name)
    resp = requests.get(url)
    if resp.status_code != 200:
        return []
    return parse_packages_from_html(resp.text)


def main(package_name=''):
    try:
        package_data = get_package_data(package_name)
    except ValueError as e:
        error_text = colored('No such package "%s"' % package_name, 'red')
        print(error_text)
        return

    releases = package_data['releases']
    show_package_info(package_data)
    most_popular_count = 0
    most_popular_release = None
    most_recent_release = None
    most_recent_date = EPOCH_BEGIN

    try:
        versions = sorted(releases.keys(), reverse=True, key=parse_version)
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
