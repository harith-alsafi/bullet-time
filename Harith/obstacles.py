import pygame
import random

from pygame.locals import *

# Initialize Pygame
pygame.init()

def obstacle_spawner(SCREEN_WIDTH,SCREEN_HEIGHT):
    # Set up obstacles
    num_obstacles = 10
    obstacle_width = 30
    obstacle_height = 30
    obstacles = []

    # Populate obstacles array
    for i in range(num_obstacles):
        x = random.randint(0, SCREEN_WIDTH - obstacle_width)
        y = random.randint(0, SCREEN_HEIGHT - obstacle_height)
        obstacles.append(pygame.Rect(x, y, obstacle_width, obstacle_height))
    return obstacles

