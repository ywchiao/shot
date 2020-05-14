
from util import Table
from util import Vector2D

from logcat import LogCat

class VectorTable(Table):
    @LogCat.log_func
    def __init__(self):
        super().__init__(Vector2D)

# vector_table.py
