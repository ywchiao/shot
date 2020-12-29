
from component import config
from component import sprite_manager
from component import ui

from util import Node

from .status_bar import StatusBar

from .system import System

from logcat import LogCat

class Configure(System):
    @LogCat.log_func
    def __init__(self):
        super().__init__()

        self.on("cmd_configure", self._configure)

    @LogCat.log_func
    def _configure(self, e):
        path = config.sprites["path"]

        for sheet in config.sprites["sheet"]:
            sprite_manager.load_sprite(f"{path}/{sheet}.png")

        bar = StatusBar()

        ui.add_widget(Node(bar.entity))

# configure.py
