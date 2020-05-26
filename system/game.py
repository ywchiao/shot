
import json

from pathlib import Path

import pygame
import pygame.freetype

from component import config

from player import Player

from .system import System

from logcat import LogCat

class Game(System):
    def __init__(self):
        self._pygame_setup()

        self._configure()

        self._player = Player(
            int((config.width - 32) / 2), int((config.height - 32) / 2)
        )

    def _configure(self):
        path = Path(f"./data/scenes")

        for f in list(path.glob("./*.json")):
            with f.open as fin:
                desc = json.load(fin)

                self.emit("cmd_scene", None, desc)

    def _pygame_setup(self):
       # 初始化 pyGame 引擎
        pygame.init()

       # 取得一個計時器物件
        self._clock = pygame.time.Clock()

        pygame.display.set_caption(config.name)

        # 設定 pyGame 遊戲視窗 *大小*
        self._win = pygame.display.set_mode((config.width, config.height))

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

            self.emit("cmd_update", None)
            self.emit(
                "cmd_repaint",
                None,
                window=self._win, background=self._background
            )

            dispatcher.dispatch_event()

            # 將遊戲視窗繪製 (貼) 到螢幕上
            pygame.display.flip()

            # 設定畫面更新率是 60 fps
            self._clock.tick(60)

    @LogCat.log_func
    def start(self):
        self._loop()

        pygame.quit()

# game.py
