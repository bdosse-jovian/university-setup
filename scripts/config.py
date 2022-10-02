from datetime import datetime
from pathlib import Path


def get_week(d=datetime.today()):
    return int(d.strftime("%W"))


CURRENT_COURSE_SYMLINK = Path('~/current-course').expanduser()
CURRENT_COURSE_ROOT = CURRENT_COURSE_SYMLINK.resolve()
CURRENT_COURSE_WATCH_FILE = Path('/tmp/current-course').resolve()
ROOT = Path('~/uni/2022').expanduser()
DATE_FORMAT = '%a %d %b %Y %H:%M'
