import sys

import pygame as pg


WIDTH = 400  # ゲームウィンドウの幅
HEIGHT = 300


def main():
    pg.display.set_caption("アリつぶし")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock  = pg.time.Clock()

    kk_img = pg.image.load("ex01/fig/3.png")

    while True:        
        for event in pg.event.get():
            if event.type == pg.QUIT: return

            # マウスクリック時の動作
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                print("mouse clicked -> (" + str(x) + ", " + str(y) + ")")
                
            # マウスポインタが移動したときの動作
            if event.type == pg.MOUSEMOTION:
                x, y = event.pos
                screen.blit(kk_img, [x, y])
                #print("mouse moved   -> (" + str(x) + ", " + str(y) + ")")

        pg.display.update()
        clock.tick(60)
        
               
if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()