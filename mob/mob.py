
from random import randint

from entity import Entity
from util import Node

from event import dispatcher

from logcat import LogCat

class Mob(Node):
    @LogCat.log_func
    def __init__(self):
        super().__init__(Entity.next())

        self.visible = True
        self.movable = True

        if randint(0, 1):
            self._turn = 1
        else:
            self._turn = -1

        dispatcher.fire_event(
            "cmd_load_sprite", self.entity, frames=(2, 3)
        )

        dispatcher.on("cmd_update", self._update)

    @property
    def entity(self):
        return self._value

    def _update(self, entity):
        dispatcher.fire_event("cmd_rotate", self.entity, degree=self._turn)
        dispatcher.fire_event("cmd_forward", self.entity)

# mob.py
