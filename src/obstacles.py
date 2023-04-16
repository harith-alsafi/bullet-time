import pygame as pygame
import random as rd
from typing import List

def obstacle_spawner(screen_width,screen_height) -> List[pygame.Rect]:
    # Set up obstacles
    num_obstacles = 10
    obstacle_width = 30
    obstacle_height = 30
    obstacles:List[pygame.Rect] = []

    # Populate obstacles array
    for i in range(num_obstacles):
        x = rd.randint(0, screen_width - obstacle_width)
        y = rd.randint(0, screen_height - obstacle_height)
        obstacles.append(pygame.pygame.Rect(x, y, obstacle_width, obstacle_height))
    return obstacles
 
