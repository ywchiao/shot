
import pygame

from component import facing
from component import sprite_origin
from component import sprite_drawing

from event import dispatcher

class Rotating:
    def __init__(self):
        dispatcher.on("cmd_rotate", self._rotate)
        dispatcher.on("cmd_facing", self._turn_to)

    def _rotate(self, entity, degree=0):
        self._turn_to(entity, facing.get_value(entity).degree + degree)

    def _turn_to(self, entity, degree=0):
        sprite_drawing.update(
            entity, [
                pygame.transform.rotate(frame, degree)
                for frame in sprite_origin.get_value(entity).items
            ]
        )

        facing.update(entity, degree)

# rotating.py
