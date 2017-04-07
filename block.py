import pygame

class Block (pygame.sprite.Sprite):

	def __init__(self, image, width, height, position):
		pygame.sprite.Sprite.__init__(self)

		self.image = image
		self.image = pygame.transform.scale(self.image, (width, height))
		self.position = position
		
		self.rect = self.image.get_rect()
			
