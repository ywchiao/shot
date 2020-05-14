
import pygame
import pygame.freetype

from player import Player

from event import dispatcher

class Game:
    def __init__(self):
        self._pygame_setup()

        _, _, width, height = self._win.get_rect()

        self._player = Player(int((width - 32) / 2), int((height - 32) / 2))

    def _pygame_setup(self):
       # 初始化 pyGame 引擎
        pygame.init()

       # 取得一個計時器物件
        self._clock = pygame.time.Clock()

        pygame.display.set_caption("Shot!")

        # 設定 pyGame 遊戲視窗 *大小*
        self._win = pygame.display.set_mode((640, 480))

        # 準備遊戲視窗的 (黑色) 背景
        self._background = self._win.copy()
        self._background.fill((0, 0, 0))

        # 設定 pyGame 使用的系統字型
        self._font = pygame.freetype.SysFont("bradleyhanditc", 36)

    def _loop(self):
        game_over = False

        # 遊戲主迴圈
        while not game_over:
            for e in pygame.event.get():
                if (e.type == pygame.QUIT):
                    game_over = True
                elif (
                    (e.type == pygame.KEYDOWN) and
                    (e.key == pygame.K_ESCAPE)
                ):
                    game_over = True
                elif (e.type == pygame.KEYDOWN):
                    dispatcher.fire_event(
                        "cmd_keyboard", self._player.entity, key=e.key
                    )

            dispatcher.fire_event("cmd_update", None)
            dispatcher.fire_event(
                "cmd_repaint", None,
                window=self._win, background=self._background
            )

            dispatcher.dispatch_event()

            # 將遊戲視窗繪製 (貼) 到螢幕上
            pygame.display.flip()

            # 設定畫面更新率是 60 fps
            self._clock.tick(60)

    def start(self):
        self._loop()

        pygame.quit()

# game.py
