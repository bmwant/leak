import os
import datetime


DEBUG = bool(os.getenv("LEAK_DEBUG", default=""))
DATE_FORMAT = "%d/%m/%Y %H:%M"
EPOCH_BEGIN = datetime.datetime.fromtimestamp(0)
FIRST_COLUMN_LENGTH = 20
