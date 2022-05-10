# Stack Implementation for multiple clipboard copy paste

# With the help of this script its possible to copy multiple
# things at once and then paste them in LIFO order.

# Dependencies : pyperclip, keyboard
# Data Structure : Stack

import time
import keyboard
import pyperclip

class Stack(object):
	def __init__(self, capacity):
		self.top = -1
		self.capacity = capacity
		self.stack = []

	def __len__(self):
		return self.size()

	def __str__(self):
		if not self.isEmpty():
			stack = self.stack[::-1]
			string = str(stack[0]) + " <- top"
			for item in stack[1:]:
				string += "\n" + str(item)

			return string

		return "Empty Stack"

	def size(self):
		return self.top + 1

	def isEmpty(self):
		return self.top == -1

	def isFull(self):
		return self.top == self.capacity - 1

	def push(self, item):
		if not self.isFull():
			self.stack.append(item)
			self.top += 1
		else:
			return "stack overflow"

	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.stack.pop()

		return "stack underflow"

	def peek(self):
		if not self.isEmpty():
			return self.stack[self.top]

		return "stack underflow"


if __name__ == "__main__":
	stack = Stack(5)

	while True:
		if keyboard.is_pressed('ctrl + q'):
			break

		if keyboard.is_pressed('ctrl + c'):
			copy = pyperclip.paste()
			print(stack.push(copy))
			print(stack)

		if keyboard.is_pressed('ctrl + v'):
			pyperclip.copy(stack.pop())
			print(stack)

		time.sleep(0.2)