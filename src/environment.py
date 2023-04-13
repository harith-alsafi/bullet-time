#Load BG images
ground_image = pygame.image.load("ground.png").convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

#Multiple images for paralax effect
bg_images=[] 
for i in range(1,6):
	bg_image = pygame.image.load(f"plx-{i}.png").convert_alpha()
	bg_images.append(bg_image)
bg_width = bg_images[0].get_width()


scroll = 0 #Initial BG scrolling value

#BG drawing Function 
#BG layers are iterated and scrolled at different speeds
def draw_bg():
    for x in range(5):
        paralax_speed = 1
        for i in bg_images:
            bg_x = round((x * bg_width) - scroll * paralax_speed)
            bg_y = 0
            screen.blit(i, (bg_x, bg_y))
            if scroll < 0:
                paralax_speed += abs(scroll) / 100
            elif scroll > ENVIRONMENT_RANGE - SCREEN_WIDTH:
                paralax_speed -= (scroll - (ENVIRONMENT_RANGE - SCREEN_WIDTH)) / 100
            else:
                paralax_speed += 0.2



#Ground drawing Function
def draw_ground():
	for x in range(15):
		screen.blit(ground_image, ((x * ground_width) - scroll *2.2, SCREEN_HEIGHT - ground_height))

