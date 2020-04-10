
import math

import pygame
import pygame.freetype

class RotateSystem:
    def __init__(self):
        pass

    def update(self, surface, degree=0):
        return pygame.transform.rotate(surface, degree)

class MoveSystem:
    def __init__(self):
        pass

    def update(self, degree, drift, offset=(0, 0)):
        theta = (degree / 180) * math.pi

        drift[0] += (
            offset[0] * math.cos(theta) +
            offset[1] * math.sin(theta)
        )

        drift[1] += (
            - offset[0] * math.sin(theta) +
            offset[1] * math.cos(theta)
        )

        drift[0], x_offset = math.modf(drift[0])
        drift[1], y_offset = math.modf(drift[1])

        return (int(x_offset), int(y_offset))

class SpriteSheetComponent:
    def __init__(self):
        # 取得 sprite sheet
        sprites = pygame.image.load('./sprites.png')

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

    def clockwise(self):
        self._rotate_degree = -15

    def counter_clockwise(self):
        self._rotate_degree = 15

    def backward(self):
        self._move_step = (0, 2)

    def forward(self):
        self._move_step = (0, -2)

    def leftward(self):
        self._move_step = (-2, 0)

    def rightward(self):
        self._move_step = (2, 0)

    def stop(self):
        pass

    def pause(self):
        self._move_step = (0, 0)

    def update(self):
        self._rotate()
        self._move()

        self._sprite_idx = (self._sprite_idx + 1) % 2
        self.sprite = self._sprites[self._sprite_idx]

        self.rect = self.sprite.get_rect()
        self.rect.center = (self._x, self._y)

def main():
    # 初始化 pyGame 引擎
    pygame.init()

    # 取得一個計時器物件
    clock = pygame.time.Clock()

    # 設定 pyGame 遊戲視窗 *標題*
    pygame.display.set_caption("Shot!")

    # 設定 pyGame 遊戲視窗 *大小*
    win = pygame.display.set_mode((640, 480))

    # 準備遊戲視窗的 (黑色) 背景
    background = win.copy()
    background.fill((0, 0, 0))

    # 設定 pyGame 使用的系統字型
    font = pygame.freetype.SysFont("bradleyhanditc", 36)

    sprite_sheet = SpriteSheetComponent()

    # 計算 Sprite 置於螢幕中央時的左上角座標
    x = int((640 - 32) / 2)
    y = int((480 - 32) / 2)

    # 初始化 Player 物件，並置於螢幕中央
    player = Player(sprite_sheet, (x, y))

    key_handler = {
        pygame.K_a: player.leftward,
        pygame.K_d: player.rightward,
        pygame.K_e: player.clockwise,
        pygame.K_f: player.backward,
        pygame.K_p: player.pause,
        pygame.K_q: player.counter_clockwise,
        pygame.K_s: player.backward,
        pygame.K_w: player.forward,
    }

    game_over = False

    # 遊戲主迴圈
    while not game_over:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                game_over = True
            elif (
                (event.type == pygame.KEYDOWN) and
                (event.key == pygame.K_ESCAPE)
            ):
                game_over = True
            elif (
                (event.type == pygame.KEYDOWN) and
                (event.key in key_handler)
            ):
                key_handler[event.key]()

        # 清除畫面，只剩下背景
        win.blit(background, (0, 0))
        win.blit(player.sprite, player.rect)

        # 將遊戲視窗繪製 (貼) 到螢幕上
        pygame.display.flip()
        #pygame.display.update()

        player.update()

        # 設定畫面更新率是 60 fps
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

# shot.py
