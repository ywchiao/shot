
from .system import System

from logcat import LogCat

class Widget(System):
    def __init__(self):
        super().__init__()

        self.on("cmd_render", self._render)

# widget.py
