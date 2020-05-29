
from random import randint

from system import Mob

from logcat import LogCat

class Circled(Mob):
    @LogCat.log_func
    def __init__(self):
        super().__init__()

        if randint(0, 1):
            self._turn = 1
        else:
            self._turn = -1

    @LogCat.log_func
    def _update(self, entity):
        self.emit("cmd_rotate", self._entity, degree=self._turn)
        self.emit("cmd_forward", self._entity)

# circled.py
