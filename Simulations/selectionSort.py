import pygame

import random

pygame.init()

SCREEN = WIDTH, HEIGHT = 640, 480

info = pygame.display.Info()

width = info.current_w

height = info.current_h

if width >= height:

	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)else:

	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

clock = pygame.time.Clock()

FPS = 15

# COLORS **********************************************************************

WHITE = (255, 255, 255)

BLUE = (30, 144,255)

RED = (255, 0, 0)

GREEN = (0, 255, 0)

BLACK = (0, 0, 20)

heights = list(range(10, 400, 5))

random.shuffle(heights)

sorted_ = False

def selectionSort(temp):

	arr = temp

	sortedArr = []

	for i in range(len(arr)):

		min_idx = i

		for j in range(i+1, len(arr)):

			if arr[min_idx] > arr[j]:

				min_idx = j

    

		arr[i], arr[min_idx] = arr[min_idx], arr[i]

		sortedArr.append([i for i in arr])

	return sortedArr

aindex = 0

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

			if event.key == pygame.K_s:

				arr = heights

				sorted_ = True

			if event.key == pygame.K_r:

				random.shuffle(heights)

				sorted_ = False

	if sorted_:

		for i in range(len(arr)):

			min_idx = i

			for j in range(i+1, len(arr)):

				if arr[min_idx] > arr[j]:

					min_idx = j

	    

			arr[i], arr[min_idx] = arr[min_idx], arr[i]

		

			for index, height in enumerate(arr):

				pygame.draw.rect(win, WHITE, ((20 + 10*index), HEIGHT - 20 - height, 5, height) )

				

				pygame.display.update()

	else:

		for index, height in enumerate(heights):

			pygame.draw.rect(win, WHITE, ((20 + 10*index), HEIGHT - 20 - height, 5, height) )

	clock.tick(FPS)

	pygame.display.update()

pygame.quit()
