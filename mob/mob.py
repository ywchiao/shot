
from random import randint

from system import System

from logcat import LogCat

class Mob:
    @LogCat.log_func
    def __init__(self, entity):
        super().__init__()

        self._visible = True
        self._movable = True

        if randint(0, 1):
            self._turn = 1
        else:
            self._turn = -1

        self.emit(
            "cmd_load_sprite", self.entity, frames=(2, 3)
        )

        self.on("cmd_update", self._update)

    @property
    def movable(self):
        return self._movable

    @property
    def visible(self):
        return self._visible

    @LogCat.log_func
    def set_movable(self, movable):
        self._movable = movable

    @LogCat.log_func
    def set_visible(self, visible):
        self._visible = visible

    def _update(self, entity):
        self.emit("cmd_rotate", self.entity, degree=self._turn)
        self.emit("cmd_forward", self.entity)

# mob.py
