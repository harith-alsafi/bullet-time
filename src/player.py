from __future__ import annotations
import src.constants as ct
from src.constants import pygame as pg
import typing as tp

class Player:
    rect:pg.Rect
    color:tp.Tuple[int, int, int] 
    x_start:int
    y_start:int
    width:int
    height:int
    x_move:int
    y_move:int

    def __init__(self, x_start:int, y_start:int, width:int, height:int, x_move:int, y_move:int, color:tp.Tuple[int, int, int]):
        self.height = height
        self.width = width
        self.x_start = x_start
        self.y_start = y_start
        self.color = color
        self.x_move = x_move
        self.y_move = y_move
        self.rect = pg.Rect((x_start, y_start, width, height))
    
    def draw(self, screen:pg.Surface):
        pg.draw.rect(screen, self.color, self.rect)

    def move_left(self):
        self.rect.move_ip(-self.x_move, 0)

    def move_right(self):
        self.rect.move_ip(self.x_move, 0)

    def move_up(self):
        self.rect.move_ip(0, self.y_move)

    def move_down(self):
        self.rect.move_ip(0, -self.y_move)

    def reset(self):
        self.rect.move_ip(self.x_start, self.y_start)

    @staticmethod
    def deafult() -> Player:
        return Player(ct.PLAYER_X_START, ct.PLAYER_Y_START, 
                      ct.PLAYER_WIDTH, ct.PLAYER_HEIGHT, 
                      ct.PLAYER_X_MOVE, ct.PLAYER_Y_MOVE, 
                      ct.PLAYER_COLOR)

