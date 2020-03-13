
import pygame
import pygame.freetype

def main():
    # 初始化 pyGame 引擎
    pygame.init()

    # 設定 pyGame 遊戲視窗 *標題*
    pygame.display.set_caption("Shot!")

    # 設定 pyGame 遊戲視窗 *大小*
    win = pygame.display.set_mode((640, 480))

    # 設定 pyGame 使用的系統字型
    font = pygame.freetype.SysFont("bradleyhanditc", 36)

    # 利用剛剛的字型製作一個文字橫幅
    welcome, welcome_rect = font.render("Hello pygame!", (255, 255, 255))

    # 計算文字橫幅的左上角座標
    x = int((640 - welcome_rect[2]) / 2)
    y = int((480 - welcome_rect[3]) / 2)

    game_over = False

    # 遊戲主迴圈
    while not game_over:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                game_over = True

        # 將文字橫幅繪製 (貼) 在遊戲視窗上
        win.blit(welcome, (x, y))

        # 將遊戲視窗繪製 (貼) 到螢幕上
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

# shot.py
