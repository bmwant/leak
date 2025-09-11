import sys
from contextlib import contextmanager
from functools import wraps

import requests

from leak import console, logger


@contextmanager
def dummy_context(*args, **kwargs):
    yield


def handle_requests_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.RequestException as e:
            logger.error(e)
            console.print(
                "[bold red]Unexpected network error occurred. "
                "Please try again later.[/]"
            )
            return sys.exit(1)

    return wrapper
