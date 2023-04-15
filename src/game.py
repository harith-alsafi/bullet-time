from src.player import Player
from src.constants import pygame as pg
import src.constants as ct

class Game:
    screen:pg.Surface
    player:Player
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((ct.SCREEN_WIDTH, ct.SCREEN_HEIGHT))
        self.player = Player.deafult()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)

    def check_shortuts(self):
        key = pg.key.get_pressed()
        if key[pg.K_RIGHT]:
            self.player.move_right()
        if key[pg.K_LEFT]:
            self.player.move_left()


    def run(self):
        run = True
        while run:
            self.draw()
            self.check_shortuts()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            pg.display.update()
        pg.quit()


