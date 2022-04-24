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
SKY = (18, 72, 158)
GREEN = (0, 255, 0)

x_off = 120
y_off = 150

font = pygame.font.SysFont('Cursive', 24)
font2 = pygame.font.SysFont('Cursive', 72)

def insertionSort(arr):
	states = []
	for i in range(length):
		index = 0
		while index < length-1:
			if arr[index] > arr[index+1]:
				temp = arr[index]
				arr[index] = arr[index+1]
				arr[index+1] = temp

			states.append(([j for j in arr], index, i))
			index += 1

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
		if i == states[index][1]:
			pygame.draw.rect(win, SKY, (x_off + 40*i, y_off, 40, 40))
		if i == states[index][1] + 1:
			pygame.draw.rect(win, GREEN, (x_off + 40*i, y_off, 40, 40))

		pygame.draw.rect(win, WHITE, (x_off + 40*i, y_off, 40, 40), 1)
		text = font.render(f'{states[index][0][i]}', True, WHITE)
		win.blit(text, (x_off + 40 * i + 15, y_off + 15))

		pass_text = font.render(f'pass : {states[index][2]+1}', True, WHITE)
		win.blit(pass_text, (WIDTH - pass_text.get_width() - 120, 200))


	clock.tick(FPS)
	pygame.display.update()

pygame.quit()