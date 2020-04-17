
import math

import pygame
import pygame.freetype

from component.sprite_sheet import SpriteSheet

from system.event import event_dispatcher

from player.player import Player

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

    sprite_sheet = SpriteSheet()

    # 計算 Sprite 置於螢幕中央時的左上角座標
    x = int((640 - 32) / 2)
    y = int((480 - 32) / 2)

    # 初始化 Player 物件，並置於螢幕中央
    player = Player(sprite_sheet, (x, y))

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
                event_dispatcher.fire_event(None, 'cmd_keyboard', key=e.key);

        event_dispatcher.dispatch_event()

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
