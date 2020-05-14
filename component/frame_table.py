
from util import CircularList
from util import Table

from logcat import LogCat

class FrameTable(Table):
    @LogCat.log_func
    def __init__(self):
        super().__init__(CircularList)

# frame_table.py
