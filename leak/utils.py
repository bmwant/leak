import sys
from contextlib import contextmanager
from functools import wraps
from typing import Any, Callable, Generator

import requests

from leak import logger, ui


@contextmanager
def dummy_context(*args, **kwargs) -> Generator[None, None, None]:
    yield


def handle_requests_errors(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.RequestException as e:
            logger.error(e)
            ui.warning(
                "[bold red]Unexpected network error occurred. "
                "Please try again later.[/]"
            )
            return sys.exit(1)

    return wrapper
