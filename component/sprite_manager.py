
import pygame

class SpriteManager:
    def __init__(self):
        self._sprites = []

    def load_sprite(self, fname):
        # 取得 sprite sheet
        sprites = pygame.image.load(f"{fname}").convert_alpha()

        for i in range(3):
            self._sprites.append(
                sprites.subsurface(pygame.Rect(0, i * 32, 32, 32))
            )

            self._sprites.append(
                sprites.subsurface(pygame.Rect(32, i * 32, 32, 32))
            )

    def get_sprite(self, i):
        return self._sprites[i]

# sprite_manager.py
