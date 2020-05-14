
from util import Angle
from util import Table

from logcat import LogCat

class FacingTable(Table):
    @LogCat.log_func
    def __init__(self):
        super().__init__(Angle)

# facing_table.py
