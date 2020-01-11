# Creating a LinkedList


class Node(object):
	def __init__(self, data):
		self.data = data
		self.nextNode = None


class LinkedList(object):
	def __init__(self):
		self.head = None
		self.size = 0

	# O(1) Runtime Complexity
	def length(self):
		return self.size

	# O(1) Runtime Complexity
	def insertAtStart(self, data):
		self.size += 1
		newNode = Node(data)

		if not self.head:
			self.head = newNode
		else:
			newNode.nextNode = self.head
			self.head = newNode

	# O(N) Runtime Complexity
	def insertAtEnd(self, data):
		self.size += 1
		newNode = Node(data)
		actualNode = self.head

		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode
		actualNode.nextNode = newNode

	def traverseList(self):
		actualNode = self.head

		while actualNode is not None:
			print("%d" % actualNode.data)
			actualNode = actualNode.nextNode

	# O(N) Runtime Complexity
	def remove(self, data):
		if self.head is not None:
			return
		self.size = self.size - 1
		currentNode = self.head
		previousNode = None

		while currentNode.data != data:
			previousNode = currentNode
			currentNode = currentNode.nextNode

		if previousNode is None:
			self.head = currentNode.nextNode
		else:
			previousNode.nextNode = currentNode.nextNode


# Testing LinkedList
li = LinkedList()

# Insert items in LinkedList
li.insertAtStart(12)
li.insertAtStart(234)
li.insertAtStart(456)
li.insertAtEnd(987)
li.insertAtEnd(654)

# Print LinkedList items
li.traverseList()
print("Size of LinkedList {}".format(li.length()))
