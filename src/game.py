from src.player import Player
from src.constants import *
from src.spritesheet import SpriteSheet
from src.button import Button
import pygame
from typing import List, Literal
import time
import random

class Game:
    font:pygame.font.Font
    screen:pygame.Surface
    player:Player

    sprite_sheet_image:pygame.Surface
    sprite_sheet:SpriteSheet

    animation_list:List[pygame.Surface]
    animation_steps:int
    last_update:int
    animation_cooldown:int 
    frame:int

    scroll:int
    clock:pygame.time.Clock
    start_time:float
    elapsed_time:int

    start_img:pygame.Surface
    exit_img:pygame.Surface

    start_button:Button
    exit_button:Button

    exit:Literal[False]
    player_death:Literal[False]

    # Load background image and define the width and height of the ground image
    ground_image:pygame.Surface
    ground_width:int
    ground_height:int

    bg_images:List[pygame.Surface]
    bg_width:int

    obstacle_image:pygame.Surface
    num_obstacles:int
    obstacle_width:int
    obstacle_height:int
    obstacle_speed:int
    obstacles:List[pygame.Rect]
    no_damage:int

    # Set up COINS
    coin_image:pygame.Surface
    num_coins:int
    coin_width:int
    coin_height:int
    coin_speed:int
    coins:List[pygame.Rect]
    player_score:int

    def __init__(self) -> None:
        # Initialize Pygame
        pygame.init()

        # Initialize Pygame font
        pygame.font.init()
        self.init()
    

    def init(self):
        # Set caption for game window
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.Font(None, 30)
        pygame.display.set_caption("Gravitate")
        self.sprite_sheet_image = pygame.image.load('asset/sprite.png').convert_alpha()
        self.sprite_sheet = SpriteSheet(self.sprite_sheet_image)
        self.player = Player.deafult()
        self.animation_list = []
        self.animation_steps = 4
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.frame = 0
        for x in range(self.animation_steps):
            self.animation_list.append(self.sprite_sheet.get_image(x , 24 , 24 , 4 , BLACK))
        
        self.frame_hurt = self.sprite_sheet.get_image(3 , 24 , 24 , 4 , BLACK)
        self.scroll = 0
        self.clock = pygame.time.Clock()
        self.start_time = time.time()
        self.elapsed_time = 0

        # Load start and exit button images
        self.start_img = pygame.image.load('asset/start_btn.png').convert_alpha()
        self.exit_img = pygame.image.load('asset/exit_btn.png').convert_alpha()

        # Create instances for start and exit buttons
        self.start_button = Button(100, 15, self.start_img, 0.3)
        self.exit_button = Button(200, 15, self.exit_img, 0.3)

        # Load background image and define the width and height of the ground image
        self.ground_image = pygame.image.load("asset/ground.png").convert_alpha()
        self.ground_width = self.ground_image.get_width()
        self.ground_height = self.ground_image.get_height()

        self.player.color = GREEN

        # Define array for background images
        self.bg_images=[]

        # Append background images to the array
        for i in range(1,6):
            bg_image = pygame.image.load(f"asset/plx-{i}.png").convert_alpha()
            self.bg_images.append(bg_image)

        # Define the width of the background
        self.bg_width = self.bg_images[0].get_width()

        self.obstacle_image = pygame.image.load("asset/spike.png").convert_alpha()

        self.num_obstacles = 5
        self.obstacle_width = 45
        self.obstacle_height = 30
        self.obstacle_speed = 5
        self.obstacles = []
        self.no_damage = 0

        # Populate obstacles array

        for i in range(self.num_obstacles):
            x = SCREEN_WIDTH + i * SCREEN_WIDTH // self.num_obstacles
            y = random.randint(0, SCREEN_HEIGHT - self.obstacle_height)
            self.obstacles.append(pygame.Rect(x, y, self.obstacle_width, self.obstacle_height))

        # Set up COINS
        self.coin_image = pygame.image.load("asset/coin.png").convert_alpha()

        self.num_coins = 5
        self.coin_width = 30
        self.coin_height = 30
        self.coin_speed = 5
        self.coins = []
        self.player.score = 0

        # Populate coin array

        for i in range(self.num_coins):
            x = SCREEN_WIDTH + i * SCREEN_WIDTH // self.num_coins
            y = random.randint(0, SCREEN_HEIGHT - self.coin_height)
            self.coins.append(pygame.Rect(x, y, self.coin_width, self.coin_height))



    # Set Up timer
    def draw(self, elapsed_time,score):
        time_text = self.font.render(f"Time: {round(elapsed_time)}s",1,"white")
        self.screen.blit(time_text,(1200,10))
        score_text = self.font.render(f"Score: {round(score)} coins!",1,"white")
        self.screen.blit(score_text,(800,10))

        pygame.display.update()

    # Define function to draw the background
    def draw_bg(self):
        for x in range(5):
            speed = 1
            for i in self.bg_images:
                self.screen.blit(i, ((x * self.bg_width) - self.scroll * speed, 0))
                speed += 0.2

    # Define function to draw the ground
    def draw_ground(self):
        for x in range(15):
            self.screen.blit(self.ground_image, ((x * self.ground_width) - self.scroll * 2.2, SCREEN_HEIGHT - self.ground_height))



    def render_health_bar(self, surface, x, y, width, height, color, health_percent):
        # Calculate the width of the health bar based on the health percentage
        health_width = int(width * health_percent / 100)

        # Draw the background of the health bar
        pygame.draw.rect(surface, (0, 0, 0), (x, y, width, height), 2)

        # Draw the health bar itself
        pygame.draw.rect(surface, color, (x + 2, y + 2, health_width, height - 4))

        # Render the health text
        health_text = self.font.render(f"Health: {health_percent}%", True, (0, 0, 0))
        surface.blit(health_text, (x + width + 10, y))

    def draw(self):
        self.screen.fill((0, 0, 255))
        # pygame.draw.rect(self.screen, self.player.color, self.player.rect)
        self.player.draw(self.screen)

    def check_shortuts(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.player.move_right()
        if key[pygame.K_LEFT]:
            self.player.move_left()


    def run(self):
        run = True
        while run:
            self.draw()
            self.check_shortuts()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()
        pygame.quit()


