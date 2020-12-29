
import math

from component import facing
from component import moving_vector
from component import position

from .system import System

from logcat import LogCat

class Moving(System):
    @LogCat.log_func
    def __init__(self):
        super().__init__()

        self.on("cmd_relocate", self._relocate)
        self.on("cmd_forward", self._forward)
        self.on("cmd_backward", self._backward)

    @LogCat.log_func
    def _forward(self, e):
        entity = e.target
        moving_vector.update(entity, (0, -2))
        self._move(entity)

    @LogCat.log_func
    def _backward(self, e):
        entity = e.target

        moving_vector.update(entity, (0, 2))
        self._move(entity)

    @LogCat.log_func
    def _move(self, entity):
        pos = position.get_value(entity)

        face_to = facing.get_value(entity)
        vector = moving_vector.get_value(entity)

        self._update_position(entity, (
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
        ))

    @LogCat.log_func
    def _relocate(self, e, point):
        self._update_position(e.target, point)

    @LogCat.log_func
    def _update_position(self, entity, point):
        position.update(entity, point)

# moving.py
