# Stack Abstract data type implementation


class Stack(object):
	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.append(data)
		return data

	def pop(self):
		data = self.stack[-1]
		del self.stack[-1]
		return data

	def peek(self):
		return self.stack[-1]

	def sizeStack(self):
		return len(self.stack)


# Stack testing
st = Stack()
print("Pushed to Stack: {}".format(st.push(45)))
print("Pushed to Stack: {}".format(st.push(78)))
print("Pushed to Stack: {}".format(st.push(21)))
print("Size of Stack: {}".format(st.sizeStack()))

print("LIFO Value {}".format(st.peek()))

print("Popped: {}".format(st.pop()))
print("Popped: {}".format(st.pop()))
print("Size of Stack: {}".format(st.sizeStack()))

print("LIFO Value {}".format(st.peek()))
