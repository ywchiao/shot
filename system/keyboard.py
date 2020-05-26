
import pygame

from core import Element

from component import moving_vector

class Keyboard(Element):
    def __init__(self):
        super().__init__()

        self._handler = {
            pygame.K_a: self._leftward,
            pygame.K_d: self._rightward,
            pygame.K_e: self._clockwise,
            pygame.K_f: self._backward,
            pygame.K_p: self._pause,
            pygame.K_q: self._counter_clockwise,
            pygame.K_s: self._backward,
            pygame.K_w: self._forward,
        }

        self.on("cmd_keyboard", self._key_handler)

    def _clockwise(self, entity):
        self.emit("cmd_rotate", entity, degree=-15)

    def _counter_clockwise(self, entity):
        self.emit("cmd_rotate", entity, degree=15)

    def _backward(self, entity):
        moving_vector.update(entity, (0, 2))

    def _forward(self, entity):
        moving_vector.update(entity, (0, -2))

    def _leftward(self, entity):
        moving_vector.update(entity, (-2, 0))

    def _rightward(self, entity):
        moving_vector.update(entity, (2, 0))

    def _stop(self, entity):
        moving_vector.update(entity, (0, 0))

    def _pause(self, entity):
        moving_vector.update(entity, (0, 0))

    def _key_handler(self, entity, key):
        if key in self._handler:
            self._handler[key](entity)

# keyboard.py
