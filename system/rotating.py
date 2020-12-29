
import pygame

from component import facing
from component import sprite_origin
from component import sprite_drawing

from .system import System

class Rotating(System):
    def __init__(self):
        super().__init__()

        self.on("cmd_rotate", self._rotate)
        self.on("cmd_facing", self._turn_to)

    def _rotate(self, e, degree=0):
        self._turn_to(e, facing.get_value(e.target).degree + degree)

    def _turn_to(self, e, degree=0):
        entity = e.target

        sprite_drawing.update(
            entity, [
                pygame.transform.rotate(frame, degree)
                for frame in sprite_origin.get_value(entity).items
            ]
        )

        facing.update(entity, degree)

# rotating.py
