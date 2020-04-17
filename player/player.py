
import pygame

from system.event import event_dispatcher
from system.move_system import MoveSystem
from system.rotate_system import RotateSystem

class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, pos=(0, 0), size=(32, 32)):
        pygame.sprite.Sprite.__init__(self)

        self._images = (
          sprite_sheet.get_sprite(2),
          sprite_sheet.get_sprite(3)
        )

        self._sprite_idx = 0
        self._sprites = list(self._images)

        self.sprite = self._sprites[self._sprite_idx]
        self.rect = self.sprite.get_rect();

        self._x, self._y = pos

        self._rotate_system = RotateSystem()
        self._move_system = MoveSystem()

        self._move_step = (0, 0)
        self._move_drift = [0, 0]

        self._rotate_degree = 0
        self._direction = 0

        self._key_handler = {
            pygame.K_a: self._leftward,
            pygame.K_d: self._rightward,
            pygame.K_e: self._clockwise,
            pygame.K_f: self._backward,
            pygame.K_p: self._pause,
            pygame.K_q: self._counter_clockwise,
            pygame.K_s: self._backward,
            pygame.K_w: self._forward,
        }

        event_dispatcher.add_listener('cmd_keyboard', self)

    def _move(self):
        offset = self._move_system.update(
            self._direction, self._move_drift, self._move_step
        )

        self._x += offset[0]
        self._y += offset[1]

    def _rotate(self):
        if self._rotate_degree:
            self._direction += self._rotate_degree
            self._rotate_degree = 0

            for i in range(len(self._sprites)):
                self._sprites[i] = self._rotate_system.update(
                    self._images[i], self._direction
                )

    def _clockwise(self):
        self._rotate_degree = -15

    def _counter_clockwise(self):
        self._rotate_degree = 15

    def _backward(self):
        self._move_step = (0, 2)

    def _forward(self):
        self._move_step = (0, -2)

    def _leftward(self):
        self._move_step = (-2, 0)

    def _rightward(self):
        self._move_step = (2, 0)

    def _stop(self):
        pass

    def _pause(self):
        self._move_step = (0, 0)

    def on_event(self, e, key):
        if key in self._key_handler:
            self._key_handler[key]()

    def update(self):
        self._rotate()
        self._move()

        self._sprite_idx = (self._sprite_idx + 1) % 2
        self.sprite = self._sprites[self._sprite_idx]

        self.rect = self.sprite.get_rect()
        self.rect.center = (self._x, self._y)

# player.py
