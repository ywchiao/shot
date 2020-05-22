
import math

from component import facing
from component import moving_vector
from component import position
from component import speed

from event import dispatcher

from logcat import LogCat

class Strategy:
    @LogCat.log_func
    def __init__(self):
        dispatcher.on("cmd_update", self._update)

    @LogCat.log_func
    def _update(self, entity):
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

# stratey
