
from random import randint

from component import config

from event import dispatcher

from logcat import LogCat

class Respawn:
    @LogCat.log_func
    def __init__(self):
        dispatcher.on("cmd_respawn", self._respawn)
#        dispatcher.on("cmd_update", self._update)

    @LogCat.log_func
    def _respawn(self, entity):
        x, y = randint(0, config.width), randint(0, config.height)

        dispatcher.fire_event("cmd_relocate", entity, point=(x, y))

        dispatcher.fire_event(
            "cmd_facing", entity, degree=randint(0, 360)
        )

    @LogCat.log_func
    def _update(self, entity):
        pass

# respawn.py
