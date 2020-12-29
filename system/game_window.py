
import pygame

from .system import System

from component import config

from logcat import LogCat

class GameWindow(System):
    def __init__(self, window, background):
        super().__init__()

        self._window = window
        self._background = background

        self._ui_font = pygame.freetype.SysFont(
            config.font["family"],
            config.font["size"]
        )

        self.on("cmd_clear", self._clear_screen)

    @LogCat.log_func
    def _clear_screen(self, e):
        self._window.blit(self._background, (0, 0))

    @LogCat.log_func
    def render(self, sprite, rect):
        self._window.blit(sprite, rect)

    @LogCat.log_func
    def box(self, fps):
        sfps, rect = self._ui_font.render(f"fps: {fps}", (255, 255, 0))
        self._window.blit(sfps, (0, 0))

# game_window.py
