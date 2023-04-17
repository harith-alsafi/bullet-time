# Import required libraries
import pygame
import button
import time
import math 
import random
import spritesheet
import obstacles
from obstacles import obstacle_spawner

# Initialize Pygame
pygame.init()

# Initialize Pygame font
pygame.font.init()

# Set FPS, screen size, environment limit, font, screen color and player's health
FPS = 60 
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 432
ENVIRONMENT_LIMIT = 30000
FONT = pygame.font.Font(None, 30)

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PLAYER_HEALTH = 100
HEALTH_BAR_WIDTH = 200
HEALTH_BAR_HEIGHT = 20
HEALTH_BAR_X = 80
HEALTH_BAR_Y = 70
BG = (50, 50, 50)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# # Set caption for game window
# pygame.display.set_caption("Gravitate")

# # Load player spritesheet image and create image instance
# sprite_sheet_image = pygame.image.load('sprite.png').convert_alpha()
# sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

# # Create player animation frames instances
# animation_list =[]
# animation_steps = 4
# last_update = pygame.time.get_ticks()
# animation_cooldown = 100
# frame = 0

# for x in range(animation_steps):
# 	animation_list.append(sprite_sheet.get_image(x , 24 , 24 , 4 , BLACK))



# frame_hurt = sprite_sheet.get_image(3 , 24 , 24 , 4 , BLACK)


# # Create a function for rendering the health bar
# def render_health_bar(surface, x, y, width, height, color, health_percent):
#     # Calculate the width of the health bar based on the health percentage
#     health_width = int(width * health_percent / 100)

#     # Draw the background of the health bar
#     pygame.draw.rect(surface, (0, 0, 0), (x, y, width, height), 2)

#     # Draw the health bar itself
#     pygame.draw.rect(surface, color, (x + 2, y + 2, health_width, height - 4))

#     # Render the health text
#     health_text = FONT.render(f"Health: {health_percent}%", True, (0, 0, 0))
#     surface.blit(health_text, (x + width + 10, y))


# # Define scrolling and timing variables
# scroll = 0
# clock = pygame.time.Clock()
# start_time = time.time()
# elapsed_time = 0

# # Define player rectangle
# player = pygame.Rect((300,250,50,50))

# # Load start and exit button images
# start_img = pygame.image.load('start_btn.png').convert_alpha()
# exit_img = pygame.image.load('exit_btn.png').convert_alpha()

# # Create instances for start and exit buttons
# start_button = button.Button(100, 15, start_img, 0.3)
# exit_button = button.Button(200, 15, exit_img, 0.3)

# Set exit and player death variables to False
# exit = False
# player_death = False

# # Load background image and define the width and height of the ground image
# ground_image = pygame.image.load("ground.png").convert_alpha()
# ground_width = ground_image.get_width()
# ground_height = ground_image.get_height()

# Define color for player
# player_colour = GREEN

# # Define array for background images
# bg_images=[]

# # Append background images to the array
# for i in range(1,6):
# 	bg_image = pygame.image.load(f"plx-{i}.png").convert_alpha()
# 	bg_images.append(bg_image)
	
# # Define the width of the background
# bg_width = bg_images[0].get_width()

# # Define function to draw the background
# def draw_bg():
# 	for x in range(5):
# 		speed = 1
# 		for i in bg_images:
# 			SCREEN.blit(i, ((x * bg_width) - scroll * speed, 0))
# 			speed += 0.2

# # Define function to draw the ground
# def draw_ground():
# 	for x in range(15):
# 		SCREEN.blit(ground_image, ((x * ground_width) - scroll * 2.2, SCREEN_HEIGHT - ground_height))


# # Set up obstacles
# obstacle_image = pygame.image.load("spike.png").convert_alpha()

# num_obstacles = 5
# obstacle_width = 45
# obstacle_height = 30
# obstacle_speed = 5
# obstacles = []
# no_damage = 0

# # Populate obstacles array

# for i in range(num_obstacles):
#     x = SCREEN_WIDTH + i * SCREEN_WIDTH // num_obstacles
#     y = random.randint(0, SCREEN_HEIGHT - obstacle_height)
#     obstacles.append(pygame.Rect(x, y, obstacle_width, obstacle_height))



# # Set up COINS
# coin_image = pygame.image.load("coin.png").convert_alpha()

# num_coins = 5
# coin_width = 30
# coin_height = 30
# coin_speed = 5
# coins = []
# player_score = 0

# # Populate coin array

# for i in range(num_coins):
#     x = SCREEN_WIDTH + i * SCREEN_WIDTH // num_coins
#     y = random.randint(0, SCREEN_HEIGHT - coin_height)
#     coins.append(pygame.Rect(x, y, coin_width, coin_height))

# # Set Up timer
# def draw(elapsed_time,score):
# 	time_text = FONT.render(f"Time: {round(elapsed_time)}s",1,"white")
# 	SCREEN.blit(time_text,(1200,10))
# 	score_text = FONT.render(f"Score: {round(score)} coins!",1,"white")
# 	SCREEN.blit(score_text,(800,10))

# 	pygame.display.update()

#////////////////////////////////////////////////
#////////////////// Game LOOP //////////////////
#//////////////////////////////////////////////
#Set the value of run to True to keep the game running in a loop
run = True

#While loop that keeps the game running
while run:
	# Set the game clock to run at the FPS value
	# clock.tick(FPS)


	# # Calculate the elapsed time since the start of the game
	# elapsed_time = time.time() - start_time

	# # Call the draw_bg function to draw the background
	# draw_bg()

	# # Call the draw_ground function to draw the ground
	# draw_ground()

	# # Check if the start button is pressed and print 'START' if it is
	# if start_button.draw(SCREEN):
	# 	print('START')

	# # Check if the exit button is pressed and print 'EXIT' if it is
	# if exit_button.draw(SCREEN):
	# 	print('EXIT')
	# 	exit = True

	# # Event handling loop that checks if the user has closed the game
	# for event in pygame.event.get():
	# 	if event.type == pygame.QUIT:
	# 		run = False

	# # Reset the value of scroll to 0 if its absolute value is greater than the width of the background image
	# if abs(scroll) > (bg_width):
	# 	scroll = 0

	# render_health_bar(SCREEN, HEALTH_BAR_X, HEALTH_BAR_Y, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT, RED, PLAYER_HEALTH)

	# # Update animation
	# current_time = pygame.time.get_ticks()
	# if current_time - last_update >= animation_cooldown:
	# 	frame += 1
	# 	last_update = current_time
	# 	if frame >= len(animation_list):
	# 		frame = 0

	# # Display the player sprite at its current x and y position
	# SCREEN.blit(animation_list[frame], (player.x, player.y))

	# # Calculate the value of timer as the elapsed time
	# timer = elapsed_time

	# # Call the draw function to draw the timer
	# draw(timer,player_score)

	# # Check for collision with obstacles and decrement the player's health if there is a collision
	# if (timer - no_damage > 3):
	# 	if player.collidelist(obstacles) >= 0:
	# 		print(PLAYER_HEALTH)
	# 		player_colour = RED   # replace with a sprite switch
	# 		PLAYER_HEALTH -= 20
	# 		print(PLAYER_HEALTH)
	# 		no_damage = timer

	# # Check for collision with coin and increment player  score
	# if player.collidelist(coins) >= 0:
	# 	player_score += 1


	# # Draw obstacles
	# for obstacle in obstacles:
	# 	SCREEN.blit(obstacle_image, (obstacle.x, obstacle.y))

	# # Set the initial values of obstacles_x and obstacles_y to 0
	# obstacles_x, obstacles_y = 0, 0

	# # Set the speed of the obstacles to 5
	# speed = 5

	# # Create new obstacles
	#     # Move obstacles and check collisions
	# new_obstacles = []
	# for obstacle in obstacles:
	# 	obstacle.x -= obstacle_speed

	# 	if player.colliderect(obstacle):
	# 		running = False

	# 	if obstacle.x + obstacle_width > 0:
	# 		new_obstacles.append(obstacle)
	# 	else:
	# 		# Generate a new obstacle
	# 		x = SCREEN_WIDTH
	# 		y = random.randint(0, SCREEN_HEIGHT - obstacle_height)
	# 		new_obstacle = pygame.Rect(x, y, obstacle_width, obstacle_height)
	# 		new_obstacles.append(new_obstacle)

	# obstacles = new_obstacles
	# Check for keyboard input from the user
	# key = pygame.key.get_pressed()


	# # Draw coins
	# for coin in coins:
	# 	SCREEN.blit(coin_image, (coin.x, coin.y))
	# # Move coins and check collisions
	# new_coins = []
	# for coin in coins:
	# 	coin.x -= coin_speed

	# 	if not player.colliderect(coin):
	# 		if coin.x + coin_width > 0:
	# 			new_coins.append(coin)
	# 		else:
	# 			# Generate a new coin
	# 			x = SCREEN_WIDTH
	# 			y = random.randint(0, SCREEN_HEIGHT - coin_height)
	# 			new_coin = pygame.Rect(x, y, coin_width, coin_height)
	# 			new_coins.append(new_coin)

	# coins = new_coins



	# Check for keyboard input from the user
	# key = pygame.key.get_pressed()




	# # Move the player sprite up by 5 pixels if the user presses the up arrow key and the player is not already at the top of the screen
	# if key[pygame.K_w] or key[pygame.K_UP]:
	# 	if player.y > 65:
	# 		player.move_ip(0, -5)

	# # Move the player sprite down by 5 pixels if the user presses the down arrow key and the player is not already at the bottom of the screen
	# elif key[pygame.K_s] or key[pygame.K_DOWN]:
	# 	if player.y < 340:
	# 		player.move_ip(0, 5)

	# # Move the obstacles to the left by the value of obstacles_x
	# scroll += 5
	# obstacles_x = -speed

	# for obstacle in obstacles:
	# 	obstacle.x += obstacles_x
	# 	obstacle.y += obstacles_y

	# # Check if the player's health has reached 0 and set player_death to True if it has
	# if PLAYER_HEALTH == 0:
	# 	player_death = True

	# Check for events, such as closing the game, and set run to False if the user closes the game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	# Quit the game if the exit button is pressed or if the player dies
	if exit or player_death:
		pygame.quit()

	# Update the display to show the changes made to the screen
	pygame.display.update()

