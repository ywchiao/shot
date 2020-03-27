
import pygame
import pygame.freetype

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pass

def main():
    # 初始化 pyGame 引擎
    pygame.init()

    # 取得一個計時器物件
    clock = pygame.time.Clock()

    # 初始化 sprite sheet
    sprite_sheet = pygame.image.load("./sprites.png")
    # subsuface 切下指定的矩型 (Rect) 區域
    # pygame.Rect(left, top, width, height)
    sprite = sprite_sheet.subsurface(pygame.Rect(0, 32, 32, 32))
    player = sprite

    # 設定 pyGame 遊戲視窗 *標題*
    pygame.display.set_caption("Shot!")

    # 設定 pyGame 遊戲視窗 *大小*
    win = pygame.display.set_mode((640, 480))

    # 準備遊戲視窗的 (黑色) 背景
    background = win.copy()
    background.fill((0, 0, 0))

    # 設定 pyGame 使用的系統字型
    font = pygame.freetype.SysFont("bradleyhanditc", 36)

    # 利用剛剛的字型製作一個文字橫幅
    welcome, welcome_rect = font.render("Hello pygame!", (255, 255, 255))

    # 計算文字橫幅的左上角座標
    # x = int((640 - welcome_rect[2]) / 2)
    x = 320
    # y = int((480 - welcome_rect[3]) / 2)
    y = 240

    # 設定文字橫幅每次移動的位移
    x_step = 2
    y_step = 2

    angle = 0

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
                (event.key == pygame.K_w)
            ):
                y = y - y_step # 前進
            elif (
                (event.type == pygame.KEYDOWN) and
                (event.key == pygame.K_a)
            ):
                x = x - x_step # 左移
            elif (
                (event.type == pygame.KEYDOWN) and
                (event.key == pygame.K_s)
            ):
                y = y + y_step # 後退
            elif (
                (event.type == pygame.KEYDOWN) and
                (event.key == pygame.K_d)
            ):
                x = x + x_step # 右移
            elif (
                (event.type == pygame.KEYDOWN) and
                (event.key == pygame.K_q)
            ):
#                center = player.rect.center
                player = pygame.transform.rotate(sprite, angle)
#                player.rect.center = center

                angle += 45
            elif (
                (event.type == pygame.KEYDOWN) and
                (event.key == pygame.K_e)
            ):
#                center = player.rect.center
                player = pygame.transform.rotate(sprite, angle)
#                player.rect.center = center

                angle -= 45

        # 清除畫面，只剩下背景
        win.blit(background, (0, 0))

        # 將文字橫幅繪製 (貼) 在遊戲視窗上
        # win.blit(welcome, (x, y))
        # win.blit(sprite_sheet, (x, y))
        win.blit(player, (x, y))

        # 計算下一次文字橫幅的左上角座標
        # x += x_step
        # y += y_step

        # 限制文字橫幅不可以超過螢幕顯示範圍
        #if (y < 10) or (y + welcome_rect.height > 460):
        if (y < 10) or (y > 460):
            y_step = 0 - y_step

        #if (x < 10) or (x + welcome_rect.width > 620):
        if (x < 10) or (x > 620):
            x_step = 0 - x_step

        # 將遊戲視窗繪製 (貼) 到螢幕上
        pygame.display.flip()

        # 設定畫面更新率是 60 fps
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

# shot.py
