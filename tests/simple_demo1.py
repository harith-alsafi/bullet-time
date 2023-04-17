import pygame
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Endless Runner')

# Set up colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Set up player
player_width = 30
player_height = 30
player = pygame.Rect(50, screen_height // 2 - player_height // 2, player_width, player_height)

# Set up obstacles
num_obstacles = 5
obstacle_width = 30
obstacle_height = 30
obstacle_speed = 5
obstacles = []

for i in range(num_obstacles):
    x = screen_width + i * screen_width // num_obstacles
    y = random.randint(0, screen_height - obstacle_height)
    obstacles.append(pygame.Rect(x, y, obstacle_width, obstacle_height))

# Set up game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    # Draw player
    pygame.draw.rect(screen, GREEN, player)

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, obstacle)

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    speed = 5
    dy = 0

    if keys[K_UP]:
        dy = -speed
    if keys[K_DOWN]:
        dy = speed

    player.y += dy
    player.y = max(0, min(screen_height - player_height, player.y))

    # Move obstacles and check collisions
    new_obstacles = []
    for obstacle in obstacles:
        obstacle.x -= obstacle_speed

        if player.colliderect(obstacle):
            running = False

        if obstacle.x + obstacle_width > 0:
            new_obstacles.append(obstacle)
        else:
            # Generate a new obstacle
            x = screen_width
            y = random.randint(0, screen_height - obstacle_height)
            new_obstacle = pygame.Rect(x, y, obstacle_width, obstacle_height)
            new_obstacles.append(new_obstacle)

    obstacles = new_obstacles

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()