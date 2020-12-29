
from component import status

from .widget import Widget

from logcat import LogCat

class StatusBar(Widget):
    def __init__(self):
        super().__init__()

    def _render(self, e, screen):
        screen.box(status.fps)

# status_bar.py
