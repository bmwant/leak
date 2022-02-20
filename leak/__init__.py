import logging
import datetime


logging.basicConfig()
logger = logging.getLogger(__package__)


DATE_FORMAT = "%d/%m/%Y %H:%M"
EPOCH_BEGIN = datetime.datetime.fromtimestamp(0)
FIRST_COLUMN_LENGTH = 20
