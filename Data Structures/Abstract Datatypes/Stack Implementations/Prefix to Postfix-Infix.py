# This script can convert a prefix notation to
# infix notation 
# postfix notation

# Data Structure used : Stack

class Stack(object):
	def __init__(self, capacity):
		self.top = -1
		self.capacity = capacity
		self.stack = []

	def __len__(self):
		return self.size()

	def __str__(self):
		if not self.isEmpty():
			elements =  ''.join(self.stack)
			return f'{elements:<7}'

		return "Empty  "

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


def prefixToInfix(prefix, stack, infix=True):
	prefix = prefix[::-1]
	print(prefix)
	for char in prefix:
		if char.isalpha() or char.isdigit():
			stack.push(char)
		else:
			res = ''
			res += stack.pop()
			if infix:
				res += char
			res += stack.pop()
			if not infix:
				res += char

			stack.push(res)

	return stack.pop()


if __name__ == '__main__':
	stack = Stack(10)

	prefix1 = '*5-^622'
	prefix2 = '*-A/BC-/AKL'
	prefix3 = '*+a-bc/-de+-fgh'
	print(prefixToInfix(prefix2, stack, False))