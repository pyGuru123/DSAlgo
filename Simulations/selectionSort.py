import pygame
import random

pygame.init()
SCREEN = WIDTH, HEIGHT = 640, 480

info = pygame.display.Info()
width = info.current_w
height = info.current_h

if width >= height:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
else:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

clock = pygame.time.Clock()
FPS = 15

# COLORS **********************************************************************

WHITE = (255, 255, 255)
BLUE = (30, 144,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 20)

heights = list(range(10, 370, 5))
random.shuffle(heights)

sorting = False

def selectionSort(arr):
	for i in range(len(arr)):
		min_idx = i
		for j in range(i+1, len(arr)):
			if arr[min_idx] > arr[j]:
				min_idx = j
    
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
		
		for index, height in enumerate(heights):
			color = WHITE
			if index == i:
				color = BLUE
			elif index == min_idx:
				color = RED
			elif index < i:
				color = GREEN
			pygame.draw.rect(win, color, ((20 + 10*index), HEIGHT - 20 - height, 5, height) )
		yield True

	return arr

# GAME ************************************************************************

running = True
while running:
	win.fill(BLACK)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
				running = False

			if event.key == pygame.K_s and not sorting:
				key = selectionSort(heights)
				sorting = True

			if event.key == pygame.K_r and not sorting:
				random.shuffle(heights)
				sorting = False

	if sorting:
			try:
				next(key)
			except:
				sorting = False

	else:
		for index, height in enumerate(heights):
			pygame.draw.rect(win, WHITE, ((20 + 10*index), HEIGHT - 20 - height, 5, height) )

	clock.tick(FPS)
	pygame.display.update()

pygame.quit()