
import math

from collections import deque

from component import facing
from component import moving_vector
from component import position
from component import scene_manager

from event import dispatcher

from logcat import LogCat

class Moving:
    @LogCat.log_func
    def __init__(self):
        dispatcher.on("cmd_relocate", self._relocate)
        dispatcher.on("cmd_update", self._update)
        dispatcher.on("cmd_forward", self._forward)
        dispatcher.on("cmd_backward", self._backward)

    @LogCat.log_func
    def _forward(self, entity):
        moving_vector.update(entity, (0, -2))

    @LogCat.log_func
    def _backward(self, entity):
        moving_vector.update(entity, (0, 2))

    @LogCat.log_func
    def _move(self, entity):
        pos = position.get_value(entity)

        face_to = facing.get_value(entity)
        vector = moving_vector.get_value(entity)

        self._relocate(entity, (
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
    def _relocate(self, entity, point):
        position.update(entity, point)

    @LogCat.log_func
    def _update(self, entity):
        scene = scene_manager.get_scene("sample")

        queue = deque([scene.root])

        while queue:
            node = queue.popleft()

            if node:
                queue.extend(node.children)

                if node.value and node.movable:
                    self._move(node.entity)

# moving.py
