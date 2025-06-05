import logging

from rich.console import Console

from .settings import config

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__package__)

if config.DEBUG:
    logger.setLevel(logging.DEBUG)

console = Console(highlight=False)
rprint = console.print
