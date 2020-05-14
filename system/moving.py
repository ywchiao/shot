
import math

from component import facing
from component import moving_vector
from component import position
from component import speed
from component import moving_objects

from event import dispatcher

from logcat import LogCat

class Moving:
    @LogCat.log_func
    def __init__(self):
        dispatcher.on("cmd_move_to", self._move_to)
        dispatcher.on("cmd_update", self._update)

    @LogCat.log_func
    def _move_to(self, entity, point):
        position.update(entity, point)

    @LogCat.log_func
    def _update(self, entity):
        for entity in moving_objects.entities:
            pos = position.get_value(entity)
            face_to = facing.get_value(entity)
            vector = moving_vector.get_value(entity)

            position.update(
                entity, (
                    (
                        pos.x +
                        vector.x * math.cos(face_to.radian) +
                        vector.y * math.sin(face_to.radian)
                    ),

                    (
                        pos.y +
                        (- vector.x) * math.sin(face_to.radian) +
                        vector.y * math.cos(face_to.radian)
                    )
                )
            )

# moving.py
