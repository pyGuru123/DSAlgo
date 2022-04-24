# Insertion sort

import pygame

pygame.init()
SCREEN = WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode(SCREEN)

FPS = 30
clock = pygame.time.Clock()

BLACK = (20, 20, 20)
WHITE = (220, 220, 220)
BLUE = (0, 249, 182)
RED = (255, 0, 0)
GREEN = (0, 220, 0)

x_off = 120
y_off = 150

font = pygame.font.SysFont('Cursive', 24)
font2 = pygame.font.SysFont('Cursive', 72)

def insertionSort(arr):
	states = []
	for i in range(1, length):
		j = i
		while j > 0 and arr[j-1] > arr[j]:
			temp = arr[j-1]
			arr[j-1] = arr[j]
			arr[j] = temp

			j -= 1

			states.append(([k for k in arr], i, j))

	return states

array = [5, 2, 4, 6, 1, 3, 7, 8, 0, 9]
length = len(array)
states = insertionSort(array)

index = 0
start = pygame.time.get_ticks()

running = True
while running:
	win.fill((30, 30, 30))
	text = font.render('Insertion Sort', True, BLUE)
	win.blit(text, (WIDTH//2 - text.get_width() // 2, 20))

	end = pygame.time.get_ticks()
	if end - start > 1000:
		start = end

		if index < len(states) - 1:
			index += 1

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
				running = False

	for i in range(length):
		if i <= states[index][1]+1:
			pygame.draw.rect(win, GREEN, (x_off + 40*i, y_off, 40, 40))
		if i == states[index][2]:
			pygame.draw.rect(win, RED, (x_off + 40*i, y_off, 40, 40))

		pygame.draw.rect(win, WHITE, (x_off + 40*i, y_off, 40, 40), 1)
		text = font.render(f'{states[index][0][i]}', True, WHITE)
		win.blit(text, (x_off + 40 * i + 15, y_off + 15))

		pass_text = font.render(f'pass : {states[index][1]}', True, WHITE)
		win.blit(pass_text, (WIDTH - pass_text.get_width() - 120, 200))


	clock.tick(FPS)
	pygame.display.update()

pygame.quit()