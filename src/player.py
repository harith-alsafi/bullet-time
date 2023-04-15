from __future__ import annotations
import constants as ct
from constants import pygame as pg
import typing as tp

class Player:
    _rect:pg.Rect
    _color:tp.Tuple[int, int, int] 
    _x_start:int
    _y_start:int
    _width:int
    _height:int
    _x_move:int
    _y_move:int

    def __init__(self, x_start:int, y_start:int, width:int, height:int, x_move:int, y_move:int, color:tp.Tuple[int, int, int]):
        self._height = height
        self._width = width
        self._x_start = x_start
        self._y_start = y_start
        self._color = color
        self._x_move = x_move
        self._y_move = y_move
        self._rect = pg.Rect((x_start, y_start, width, height))
    
    def draw(self, screen:pg.Surface):
        pg.draw.rect(screen, self._color, self._rect)

    def move_left(self):
        self._rect.move_ip(-self._x_move, 0)

    def move_right(self):
        self._rect.move_ip(self._x_move, 0)

    def move_up(self):
        self._rect.move_ip(0, self._y_move)

    def move_down(self):
        self._rect.move_ip(0, -self._y_move)

    def reset(self):
        self._rect.move_ip(self._x_start, self._y_start)

    def width(self)-> int:
        return self._width

    def height(self)-> int:
        return self._height

    @staticmethod
    def deafult() -> Player:
        return Player(ct.PLAYER_X_START, ct.PLAYER_Y_START, 
                      ct.PLAYER_WIDTH, ct.PLAYER_HEIGHT, 
                      ct.PLAYER_X_MOVE, ct.PLAYER_Y_MOVE, 
                      ct.PLAYER_COLOR)

