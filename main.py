#Imports
import pygame, sys


def fancyGround():
	gameWindow.blit(ground, (groundXPos, 425))
	gameWindow.blit(ground, (groundXPos + 267, 425))


pygame.init()
'''Display Surfaces'''
displayWide = 280
displayHi = 500
groundHi = 80
gameWindow = pygame.display.set_mode((displayWide, displayHi))
bgSurface = pygame.image.load('PNG/backgroundDay.png').convert()
bgSurface = pygame.transform.scale(bgSurface, (displayWide + 10, displayHi))
ground = pygame.image.load('PNG/ground.png').convert()
ground = pygame.transform.scale(ground, (displayWide, groundHi))
groundXPos = 0
#birdySurface = pygame.image.load('PNG/blueBirdCenter.png').convert()
#birdyRect = birdySurface.get_rect(center = (100, 250))
'''Timing'''
clock = pygame.time.Clock()
'''Title Bar'''
pygame.display.set_caption('FlappyClone')
'''***Game Loop***'''
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			'''Shutdown completely'''
			sys.exit()
	'''IMAGES ON SCREEN'''
	gameWindow.blit(bgSurface, (-5, 0))
	#gameWindow.blit(birdySurface,birdyRect)
	groundXPos -= 1
	fancyGround()
	if groundXPos <= -267:
		groundXPos = 0
	'''***ABOVE HERE GET DISPLAYED***'''
	pygame.display.update()
	'''frames per second'''
	clock.tick(120)
