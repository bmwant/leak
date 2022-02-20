import logging

from . import config


logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__package__)

if config.DEBUG:
    logger.setLevel(logging.INFO)
