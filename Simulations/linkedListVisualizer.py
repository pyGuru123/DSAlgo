import pygame

pygame.init()
SCREEN = WIDTH, HEIGHT = 640, 380

info = pygame.display.Info()
width = info.current_w
height = info.current_h

if width >= height:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
else:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

clock = pygame.time.Clock()
FPS = 60

# COLORS **********************************************************************

WHITE = (255, 255, 255)
BLUE = (30, 144,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 20)

font = pygame.font.SysFont('Arial', 15)

textArray = [
	'1. Insert at Front',
	'2. Insert at Rear',
	'3. Delete from Front',
	'4. Delete from Rear',
	'5. Get Linked List Size'
]


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.start = None
		self.initial = 40
		self.length = 0

	def insertFront(self, data):
		node = Node(data)
		if self.start is None:
			self.start = node
		else:
			node.next = self.start
			self.start = node
		self.length += 1

	def insertEnd(self, data):
		node = Node(data)
		ptr = self.start
		while (ptr.next is not None):
			ptr = ptr.next
		ptr.next = data
		self.length += 1

	def size(self):
		return self.length

radius = 15
def displayList(head):
	size = ll.size()
	initial = WIDTH // 2 - ((size * 50) // 2)
	i = 0
	while (head is not None):
		rect = pygame.draw.circle(win, WHITE, (initial + (50 * i), 100), radius)
		pygame.draw.circle(win, RED, (initial + (50 * i), 100), radius, 1)
		text = font.render(f'{head.data}', True, RED)
		win.blit(text, (rect.centerx-7, rect.centery-10))
		head = head.next
		i += 1

ll = LinkedList()
ll.insertFront(5)
ll.insertFront(10)
ll.insertFront(20)

data = ''
takeInput = False

running = True
while running:
	win.fill(BLACK)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
				running = False

			if event.key == pygame.K_1:
				mode = 1
				takeInput = True

			if event.key == pygame.K_1:
				print("pressed 2")

			if event.key == pygame.K_1:
				print("pressed 3")

			if event.key == pygame.K_1:
				print("pressed 4")

			if event.key == pygame.SPACE:
				if mode == 1:
					ll.insertFront(int(data))
				takeInput = False
				data = ''

			if takeInput:
				data += pygame.key.name(event.key)


	displayList(ll.start)
	pygame.draw.line(win, WHITE, (0, 180), (WIDTH, 180), 3)
	for index, text in enumerate(textArray):
		textImage = font.render(text, True, WHITE)
		win.blit(textImage, (40, (200 + (30*index))))

	pygame.draw.rect(win, WHITE, (0, 0, WIDTH, HEIGHT), 3)
				
	clock.tick(FPS)
	pygame.display.update()

pygame.quit()