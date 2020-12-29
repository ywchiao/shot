
from random import randint

from component import config
from component import facing
from component import position

from system import Mob

from logcat import LogCat

class Wave(Mob):
    @LogCat.log_func
    def __init__(self):
        super().__init__()

        if randint(0, 1):
            self._turn = 1
        else:
            self._turn = -1

    @LogCat.log_func
    def _update(self, entity):
        degree = facing.get_value(self._entity).degree

        if degree > (self._degree + 210) % 360:
            self._turn = -1
        elif degree < (self._degree + 120) % 360:
            self._turn = 1

        self.emit("cmd_rotate", self._entity, degree=self._turn)
        self.emit("cmd_forward", self._entity)

# wave.py
