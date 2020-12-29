
import pygame

from .system import System

from component import moving_vector

class Keyboard(System):
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

    def _clockwise(self, e):
        self.emit("cmd_rotate", e.target, degree=-15)

    def _counter_clockwise(self, e):
        self.emit("cmd_rotate", e.target, degree=15)

    def _backward(self, e):
        moving_vector.update(e.target, (0, 2))

    def _forward(self, e):
        moving_vector.update(e.target, (0, -2))

    def _leftward(self, e):
        moving_vector.update(e.target, (-2, 0))

    def _rightward(self, e):
        moving_vector.update(e.target, (2, 0))

    def _stop(self, e):
        moving_vector.update(e.target, (0, 0))

    def _pause(self, e):
        moving_vector.update(e.target, (0, 0))

    def _key_handler(self, e, key):
        if key in self._handler:
            self._handler[key](e.target)

# keyboard.py
