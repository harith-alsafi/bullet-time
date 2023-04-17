from src.constants import *
from src.spritesheet import SpriteSheet
from src.button import Button
import pygame
from typing import List, Literal, Tuple
import time
import random

class Game:
    delimeter = "\\"
    font:pygame.font.Font
    screen:pygame.Surface

    sprite_sheet_image:pygame.Surface
    sprite_sheet:SpriteSheet

    animation_list:List[pygame.Surface]
    animation_steps:int
    last_update:int
    animation_cooldown:int 
    frame:int

    frame_hurt:pygame.Surface

    scroll:int
    clock:pygame.time.Clock
    start_time:float
    elapsed_time:int

    player:pygame.Rect

    start_img:pygame.Surface
    exit_img:pygame.Surface

    start_button:Button
    exit_button:Button

    exit:bool
    player_death:bool

    # Load background image and define the width and height of the ground image
    ground_image:pygame.Surface
    ground_width:int
    ground_height:int

    player_color:Tuple[int, int, int]

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
    player_health:int

    run:bool

    def __init__(self) -> None:
        # Initialize Pygame
        pygame.init()

        # Initialize Pygame font
        pygame.font.init()

        # Set caption for game window
        pygame.display.set_caption("Gravitate")
        self.font = pygame.font.Font(None, 30)
        self.screen =  pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.init()
    
    def load_img(self, file:str) -> pygame.Surface:
        return pygame.image.load('asset'+self.delimeter+file)

    def init_animation_frame(self):

        # Load player spritesheet image and create image instance
        self.sprite_sheet_image = self.load_img('sprite.png').convert_alpha()
        self.sprite_sheet = SpriteSheet(self.sprite_sheet_image)

        # Create player animation frames instances
        self.animation_list =[]
        self.animation_steps = 4
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100
        self.frame = 0

        for x in range(self.animation_steps):
            self.animation_list.append(self.sprite_sheet.get_image(x , 24 , 24 , 4 , BLACK))

        self.frame_hurt = self.sprite_sheet.get_image(3 , 24 , 24 , 4 , BLACK)

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

    def init_scroll(self):
        # Define scrolling and timing variables
        self.scroll = 0
        self.clock = pygame.time.Clock()
        self.start_time = time.time()
        self.elapsed_time = 0

    def init_buttons(self):
        # Load start and exit button images
        self.start_img = self.load_img('start_btn.png').convert_alpha()
        self.exit_img = self.load_img('exit_btn.png').convert_alpha()

        # Create instances for start and exit buttons
        self.start_button = Button(100, 15, self.start_img, 0.3)
        self.exit_button = Button(200, 15, self.exit_img, 0.3)

    def init_player(self):
        # Define player rectangle
        self.player = pygame.Rect((PLAYER_X_START,PLAYER_Y_START,PLAYER_WIDTH,PLAYER_HEIGHT))
        self.exit = False
        self.player_death = False
        self.player_color = GREEN

    def init_ground(self):
        # Load background image and define the width and height of the ground image
        self.ground_image = self.load_img("ground.png").convert_alpha()
        self.ground_width = self.ground_image.get_width()
        self.ground_height = self.ground_image.get_height()

    def init_background(self):
        # Define array for background images
        self.bg_images=[]

        # Append background images to the array
        for i in range(1,6):
            bg_image = self.load_img(f"plx-{i}.png").convert_alpha()
            self.bg_images.append(bg_image)
            
        # Define the width of the background
        self.bg_width = self.bg_images[0].get_width()


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

    def init_obstacle(self):
        # Set up obstacles
        self.obstacle_image = self.load_img("spike.png").convert_alpha()

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


    def init_coins(self):
        # Set up COINS
        self.coin_image = self.load_img("coin.png").convert_alpha()

        self.num_coins = 5
        self.coin_width = 30
        self.coin_height = 30
        self.coin_speed = 5
        self.coins = []
        self.player_score = 0

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


    def init(self):
        self.init_animation_frame()
        self.init_scroll()
        self.init_player()
        self.init_buttons()
        self.init_ground()
        self.init_background()
        self.init_obstacle()
        self.init_coins()
        self.player_health = 100

    def check_shortuts(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.player.move_right()
        if key[pygame.K_LEFT]:
            self.player.move_left()

    def run_time(self):
        self.clock.tick(FPS)
        self.elapsed_time = time.time() - self.start_time

    def draw_enviroment(self):
        self.draw_bg()
        self.draw_ground()

    def check_buttons(self):
        # Check if the start button is pressed and print 'START' if it is
        if self.start_button.draw(self.screen):
            print('START')

        # Check if the exit button is pressed and print 'EXIT' if it is
        if self.exit_button.draw(self.screen):
            print('EXIT')
            self.exit = True

    def check_events(self):  
        # Event handling loop that checks if the user has closed the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False


    def check_scroll(self):
        # Reset the value of scroll to 0 if its absolute value is greater than the width of the background image
        if abs(self.scroll) > (self.bg_width):
            self.scroll = 0

    def update_animation(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = self.current_time
            if self.frame >= len(self.animation_list):
                self.frame = 0
        self.screen.blit(self.animation_list[self.frame], (self.player.x, self.player.y))
    
    def update_timer(self):
        # Calculate the value of timer as the elapsed time
        self.timer = self.elapsed_time

        # Call the draw function to draw the timer
        self.draw(self.timer,self.player_score)

    def check_collision(self):
        # Check for collision with obstacles and decrement the player's health if there is a collision
        if (self.timer - self.no_damage > 3):
            if self.player.collidelist(self.obstacles) >= 0:
                print(self.player_health)
                self.player_colour = RED   # replace with a sprite switch
                self.player_health -= 20
                print(self.player_health)
                self.no_damage = self.timer

        # Check for collision with coin and increment player  score
        if self.player.collidelist(self.coins) >= 0:
            self.player_score += 1

    def draw_obstacle(self):
        # Draw obstacles
        for obstacle in self.obstacles:
            self.screen.blit(self.obstacle_image, (obstacle.x, obstacle.y))

        # Set the initial values of obstacles_x and obstacles_y to 0
        self.obstacles_x, self.obstacles_y = 0, 0

        # Set the speed of the obstacles to 5
        self.speed = 5

        # Create new obstacles
        # Move obstacles and check collisions
        self.new_obstacles = []
        for obstacle in self.obstacles:
            obstacle.x -= self.obstacle_speed

            if self.player.colliderect(obstacle):
                self.running = False

            if obstacle.x + self.obstacle_width > 0:
                self.new_obstacles.append(obstacle)
            else:
                # Generate a new obstacle
                x = SCREEN_WIDTH
                y = random.randint(0, SCREEN_HEIGHT - self.obstacle_height)
                new_obstacle = pygame.Rect(x, y, self.obstacle_width, self.obstacle_height)
                self.new_obstacles.append(new_obstacle)

        self.obstacles = self.new_obstacles


    def draw_coins(self):
        # Draw coins
        for coin in self.coins:
            self.screen.blit(self.coin_image, (coin.x, coin.y))
        # Move coins and check collisions
        self.new_coins = []
        for coin in self.coins:
            coin.x -= self.coin_speed

            if not self.player.colliderect(coin):
                if coin.x + self.coin_width > 0:
                    self.new_coins.append(coin)
                else:
                    # Generate a new coin
                    x = SCREEN_WIDTH
                    y = random.randint(0, SCREEN_HEIGHT - self.coin_height)
                    new_coin = pygame.Rect(x, y, self.coin_width, self.coin_height)
                    self.new_coins.append(new_coin)

        self.coins = self.new_coins


    def check_keys(self):
      	# Move the player sprite up by 5 pixels if the user presses the up arrow key and the player is not already at the top of the screen
        if self.key[pygame.K_w] or self.key[pygame.K_UP]:
            if self.player.y > 65:
                self.player.move_ip(0, -5)

        # Move the player sprite down by 5 pixels if the user presses the down arrow key and the player is not already at the bottom of the screen
        elif self.key[pygame.K_s] or self.key[pygame.K_DOWN]:
            if self.player.y < 340:
                self.player.move_ip(0, 5)

        # Move the obstacles to the left by the value of obstacles_x
        self.scroll += 5
        self.obstacles_x = -self.speed

        for obstacle in self.obstacles:
            obstacle.x += self.obstacles_x
            obstacle.y += self.obstacles_y

        # Check if the player's health has reached 0 and set player_death to True if it has
        if self.player_health == 0:
            self.player_death = True
    
    def finalize_run(self):
        # Quit the game if the exit button is pressed or if the player dies
        if self.exit or self.player_death:
            pygame.quit()

        # Update the display to show the changes made to the screen
        pygame.display.update()

    def run_game(self):
        self.run = True
        while self.run:
            self.run_time()
            self.draw_enviroment()
            self.check_buttons()
            self.check_events()
            self.check_scroll()
            self.render_health_bar(self.screen, HEALTH_BAR_X, HEALTH_BAR_Y, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT, RED, self.player_health)
            self.update_animation()
            self.update_timer()
            self.check_collision()
            self.draw_obstacle()
            self.key = pygame.key.get_pressed()
            self.draw_coins()
            self.key = pygame.key.get_pressed()
            self.check_keys()
            self.check_events()
            self.finalize_run()
            
        pygame.quit()


