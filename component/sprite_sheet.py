
import pygame

class SpriteSheet:
    def __init__(self):
        # 取得 sprite sheet
        sprites = pygame.image.load('./resources/png/sprites.png')

        self._sprites = []

        for i in range(3):
            self._sprites.append(
                sprites.subsurface(pygame.Rect(0, i * 32, 32, 32))
            )

            self._sprites.append(
                sprites.subsurface(pygame.Rect(32, i * 32, 32, 32))
            )

    def get_sprite(self, i):
        return self._sprites[i]

# sprite_sheet.py
