
from entity import Entity

from system import System

from logcat import LogCat

class Player(System):
    @LogCat.log_func
    def __init__(self, x, y):
        super().__init__()

#        moving_objects.register(self.entity)
#        viewable_objects.register(self.entity)

        self.emit(
            "cmd_load_sprite", self.entity, frames=(2, 3)
        )

        self.emit(
            "cmd_relocate", self.entity, point=(x, y)
        )

        self.emit(
            "cmd_facing", self.entity, degree=0
        )

# player.py
