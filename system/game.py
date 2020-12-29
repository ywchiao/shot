
import time

import pygame
import pygame.freetype

from component import config

from .game_window import GameWindow

from .system import System

from .configure import Configure
from .heartbeat import Heartbeat
from .keyboard import Keyboard
from .moving import Moving
from .painting import Painting
from .respawn import Respawn
from .rotating import Rotating

from .mob_factory import MobFactory
from .scene_factory import SceneFactory

from logcat import LogCat

class Game(System):
    def __init__(self):
        super().__init__()

        self._pygame_setup()

        self._setup()

#        self._player = Player(
#            int((config.width - 32) / 2), int((config.height - 32) / 2)
        #)

    def _setup(self):
        for system in (
           Configure, Heartbeat, Keyboard, Moving, Painting, Rotating,
           Respawn, MobFactory, SceneFactory,
        ):
            system()

        self.emit("cmd_configure", None)
        self.emit("cmd_scene_change", None, scene=config.open_scene)

    def _pygame_setup(self):
       # 初始化 pyGame 引擎
        pygame.init()

       # 取得一個計時器物件
        self._clock = pygame.time.Clock()

        pygame.display.set_caption(config.name)

        # 設定 pyGame 遊戲視窗 *大小*
        win = pygame.display.set_mode((config.width, config.height))

        # 準備遊戲視窗的 (黑色) 背景
        background = pygame.Surface((config.width, config.height))
#        background = win.copy()
#        background.fill((0, 0, 0))

        # 建立一個新的 GameWindow 物件
        self._window = GameWindow(win, background)

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
#                elif (e.type == pygame.KEYDOWN):
                    #self.emit(
                    #    "cmd_keyboard", self._player.entity, key=e.key
                    #)

            self.emit(
                "cmd_heartbeat",
                None,
                ticks=self._clock.get_time(),
                fps=self._clock.get_fps()
            )
            self.emit("cmd_update", None)
            self.emit("cmd_repaint", None, screen=self._window)

            self._dispatcher.dispatch()

            # 將遊戲視窗繪製 (貼) 到螢幕上
            pygame.display.flip()

            # 設定畫面更新率是 60 fps
            self._clock.tick(60)

    @LogCat.log_func
    def start(self):
        self._loop()

        pygame.quit()

# game.py
