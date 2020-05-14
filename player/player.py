
from entity import Entity

from component import moving_objects
from component import viewable_objects

from event import dispatcher

from logcat import LogCat

class Player(Entity):
    @LogCat.log_func
    def __init__(self, x, y):
        super().__init__()

        moving_objects.register(self.entity)
        viewable_objects.register(self.entity)

        dispatcher.fire_event(
            "cmd_load_sprite", self.entity, frames=(2, 3)
        )

        dispatcher.fire_event(
            "cmd_move_to", self.entity, point=(x, y)
        )

        dispatcher.fire_event(
            "cmd_turn_to", self.entity, degree=0
        )

# player.py
