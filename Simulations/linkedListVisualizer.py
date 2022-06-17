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
font1 = pygame.font.SysFont("Arial", 20, True)
cross = font1.render("X", True, RED)
visualizer = font1.render("Linked List Visualizer", True, BLUE)

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
		ptr.next = node
		self.length += 1

	def removeFront(self):
		if self.size():
			ptr = self.start
			self.start = self.start.next
			self.length -= 1
			return ptr.data
		return None

	def removeRear(self):
		if self.size():
			data = None
			if self.start.next is None:
				data = self.start.data
				self.start = None
			else:
				ptr = self.start
				while(ptr.next.next is not None):
					ptr = ptr.next
				temp = ptr.next
				ptr.next = None
				data = temp.data
			self.length -= 1
			return data
		return None

	def size(self):
		return self.length

radius = 15
def displayList(head):
	size = ll.size()
	initial = WIDTH // 2 - ((size * 50) // 2)
	i = 0
	if head is None:
		rect = pygame.draw.circle(win, WHITE, (initial + (50 * i), 110), radius)
		pygame.draw.circle(win, RED, (initial + (50 * i), 110), radius, 1)
		pygame.draw.line(win, WHITE, (rect.right, rect.centery), (rect.right+30, rect.centery), 2)
	else:
		while (head is not None):
			rect = pygame.draw.circle(win, WHITE, (initial + (50 * i), 110), radius)
			pygame.draw.circle(win, RED, (initial + (50 * i), 110), radius, 1)
			text = font.render(f'{head.data}', True, RED)
			win.blit(text, (rect.centerx-7, rect.centery-10))
			pygame.draw.line(win, WHITE, (rect.right, rect.centery), (rect.right+30, rect.centery), 2)
			head = head.next
			i += 1
	win.blit(cross, (rect.right+30, rect.centery-12))

ll = LinkedList()

mode = None
data = ''
msg = ''
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

			if takeInput:
				if pygame.key.name(event.key).isdigit():
					data += pygame.key.name(event.key)

			if event.key == pygame.K_1 and not mode:
				mode = 1
				takeInput = True
				msg = ''

			if event.key == pygame.K_2 and not mode:
				mode = 2
				takeInput = True
				msg = ''

			if event.key == pygame.K_3 and not mode:
				d = ll.removeFront()
				if d:
					msg = f'Front Element deleted : {d}'

			if event.key == pygame.K_4 and not mode:
				d = ll.removeRear()
				if d:
					msg = f'Rear Element deleted : {d}'

			if event.key == pygame.K_5 and not mode:
				msg = f'Linked List Size : {ll.size()}'

			if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
				if mode == 1 and data:
					ll.insertFront(int(data))
				if mode == 2 and data:
					ll.insertEnd(int(data))
				mode = None
				takeInput = False
				data = ''

	win.blit(visualizer, (WIDTH//2-visualizer.get_width()//2, 30))
	displayList(ll.start)
	pygame.draw.line(win, WHITE, (0, 180), (WIDTH, 180), 3)
	for index, text in enumerate(textArray):
		color = WHITE
		if mode and index == mode - 1:
			color = GREEN
		textImage = font.render(text, True, color)
		win.blit(textImage, (40, (200 + (30*index))))

	if takeInput:
		datatext = font.render(f'Enter data : {data}', True, WHITE)
		win.blit(datatext, (WIDTH//2, HEIGHT//2+50))

	if msg:
		datatext = font.render(f'{msg}', True, WHITE)
		win.blit(datatext, (WIDTH//2, HEIGHT//2+50))

	pygame.draw.rect(win, WHITE, (0, 0, WIDTH, HEIGHT), 3)
				
	clock.tick(FPS)
	pygame.display.update()

pygame.quit()