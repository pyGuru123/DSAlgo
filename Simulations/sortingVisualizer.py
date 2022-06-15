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
GREEN = (0, 205, 0)
BLACK = (0, 0, 0)

colors = [WHITE, (200, 200, 200), (150, 150, 150)]
colors2 = [GREEN, (34, 139, 34), (144, 238, 144)]

# Font ***********************************************************************

font = pygame.font.SysFont("Arial", 15)
insertion_text = font.render("I: Insertion Sort", True, WHITE)
bubble_text = font.render("B: Bubble Sort", True, WHITE)
selection_text = font.render("S: Selection Sort", True, WHITE)

SIDEPAD = 40
TOPPAD = 100

n = 100
minh = 10
maxh = 200

def getRandomHeights():
	heights = []
	for i in range(n):
		ht = random.randint(minh, maxh)
		heights.append(ht)
	random.shuffle(heights)
	return heights
heights = getRandomHeights()
width = (WIDTH - SIDEPAD) // len(heights)
height = (HEIGHT - TOPPAD) // (max(heights) - min(heights))

sorting = False

def draw(arr, i, j):
	for index, ht in enumerate(heights):
			color = colors[index%3]
			if index == i:
				color = BLUE
			elif index == j:
				color = RED
			elif index < i:
				color = colors2[index % 3]
			pygame.draw.rect(win, color, ((20 + width*index), HEIGHT - (ht * height), width, height * ht) )

def selectionSort(arr):
	for i in range(len(arr)):
		min_idx = i
		for j in range(i+1, len(arr)):
			if arr[min_idx] > arr[j]:
				min_idx = j
    
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
		draw(arr, i, min_idx)
		
		yield True

	return arr
	
def bubbleSort(arr):
	for i in range(len(arr)-1):
		for j in range(len(arr) - i -1):
			if arr[j] > arr[j+1]:
				m = j
				arr[j], arr[j+1] = arr[j+1], arr[j]
				
		draw(arr, m, m+1)
		yield True
				
	# return arr
	print(arr)

def insertionSort(arr):
	for i in range(len(arr)):
		key = arr[i]
		j = i-1
		while(j>=0 and arr[j] > key):
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
		draw(arr, i, j)
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
				
			if event.key == pygame.K_b and not sorting:
				key = bubbleSort(heights)
				sorting = True

			if event.key == pygame.K_i and not sorting:
				key = insertionSort(heights)
				sorting = True

			if event.key == pygame.K_r and not sorting:
				heights = getRandomHeights()
				width = (WIDTH - SIDEPAD) // len(heights)
				height = (HEIGHT - TOPPAD) // (max(heights) - min(heights))
				sorting = False

	n_text = font.render(f"n : {n}", True, WHITE)
	minh_text = font.render(f"minh : {minh}", True, WHITE)
	maxh_text = font.render(f"maxh : {maxh}", True, WHITE)

	win.blit(insertion_text, (20, 20))
	win.blit(selection_text, (20, 50))
	win.blit(bubble_text, (20, 80))
	win.blit(n_text, (300, 20))
	win.blit(minh_text, (400, 20))
	win.blit(maxh_text, (500, 20))

	if sorting:
			try:
				next(key)
			except:
				sorting = False
	else:
		for index, ht in enumerate(heights):
			color = colors[index % 3]
			pygame.draw.rect(win, color, ((20 + width*index), HEIGHT - height * ht, width, height * ht) )

	clock.tick(FPS)
	pygame.display.update()

pygame.quit()