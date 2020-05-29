
from component import window_manager

from .system import System

from logcat import LogCat

class GameWindow(System):
    def __init__(self, window, background):
        super().__init__()

        window_manager.register(self)

        self._window = window
        self._background = background

        self.on("cmd_clear", self._clear_screen)

    @LogCat.log_func
    def _clear_screen(self, entity):
        self._window.blit(self._background, (0, 0))

    @LogCat.log_func
    def render(self, sprite, rect):
        self._window.blit(sprite, rect)

# game_window.py
