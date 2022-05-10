# This script can convert a infix notation to
# prefix notation 
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

precedence = {
	'(' : -1,
	'+' : 0,
	'-' : 0,
	'*' : 1,
	'/' : 1,
	'^' : 2
}

def infixToPostfix(infix, stack):
	postfix = ''
	for char in infix:
		if char.isalpha():
			postfix += char
		else:
			if stack.isEmpty() or char == '(':
				stack.push(char)
			else:
				if char == ')':
					while stack.peek() != '(':
						postfix += stack.pop()
					stack.pop()
				else:
					if precedence[char] > precedence[stack.peek()]:
						stack.push(char)
					else:
						postfix += stack.pop()
						stack.push(char)

	while not stack.isEmpty():
		postfix += stack.pop()

	return postfix

if __name__ == '__main__':
	stack = Stack(6)

	infix1 = 'A+B*C'
	infix2 = 'A+(B*C-(D/E^F)*G)*H'
	print(infixToPostfix(infix1, stack))
	print(infixToPostfix(infix2, stack))