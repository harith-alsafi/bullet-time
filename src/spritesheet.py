import pygame

class SpriteSheet():
	def __init__(self, image):
		self.sheet = image

	# Define a function to get player image from the spritesheet
	def get_image(self, frame, width, height, scale, colour) -> pygame.Surface:
		image:pygame.Surface = pygame.Surface((width,height)).convert_alpha()
		image.blit(self.sheet, (0,0), ((frame * width),0, width, height) )
		image = pygame.transform.scale(image,(width*scale, height*scale))
		image.set_colorkey(colour)
		return image