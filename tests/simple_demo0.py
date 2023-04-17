import pygame
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 1500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Moving Obstacles')

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up obstacles
num_obstacles = 10
obstacle_width = 30
obstacle_height = 30
obstacles = []

# Populate obstacles array
for i in range(num_obstacles):
    x = random.randint(0, screen_width - obstacle_width)
    y = random.randint(0, screen_height - obstacle_height)
    obstacles.append(pygame.Rect(x, y, obstacle_width, obstacle_height))

# Set up game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, obstacle)

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Move obstacles based on pressed keys
    obstacles_x, obstacles_y = 0, 0
    speed = 5


    if keys[K_a]:
        obstacles_x = speed
    if keys[K_d]:
        obstacles_x = -speed

    for obstacle in obstacles:
        obstacle.x += obstacles_x
        obstacle.y += obstacles_y

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
