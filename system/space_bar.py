
from component import status

from .system import Widget

from logcat import LogCat

class SpaceBar(Widget):
    def __init__(self):
        super().__init__()

        self.on("cmd_render", self._render)

    @LogCat.log_func
    def _render(self, e, screen):
        screen.box(static.fps)

# space_bar.py
