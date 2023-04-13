import constants as ct
from constants import pygame as pg

class Player:
    rect:pg.Rect = pg.Rect((ct.PLAYER_X_START, ct.PLAYER_Y_START, ct.PLAYER_WIDTH, ct.PLAYER_WIDTH))
    x:int = ct.PLAYER_X_START
    y:int = ct.PLAYER_Y_START

    def init(self):
        return
    
    def draw(self, screen:pg.Surface):
        pg.draw.rect(screen, ct.PLAYER_COLOR, self.rect)

    def move_up(self, screen:pg.Surface):
        self.rect.move_ip()

