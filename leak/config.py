import os
import datetime


DEBUG = bool(os.getenv("LEAK_DEBUG", default=""))
DATE_FORMAT = "%Y/%m/%d %H:%M"
EPOCH_BEGIN = datetime.datetime.fromtimestamp(0)
SHOW_LATEST_RELEASES = 12
SHOW_PAGER = 30
PANEL_WIDTH = 70
