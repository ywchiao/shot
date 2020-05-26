
from random import randint

from component import config

from core import Element

from logcat import LogCat

class Respawn(Element):
    @LogCat.log_func
    def __init__(self):
        super().__init__()

        self.on("cmd_respawn", self._respawn)

    @LogCat.log_func
    def _respawn(self, entity):
        x, y = randint(0, config.width), randint(0, config.height)

        self.emit("cmd_relocate", entity, point=(x, y))

        self.emit(
            "cmd_facing", entity, degree=randint(0, 360)
        )

    @LogCat.log_func
    def _update(self, entity):
        pass

# respawn.py
