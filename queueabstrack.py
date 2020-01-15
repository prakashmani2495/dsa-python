# Queue Absract data type implementation


class Queue(object):
	def __init__(self):
		self.queue = []

	def enqueue(self, data):
		self.queue.append(data)
		return data

	def dequeue(self):
		data = self.queue[0]
		del self.queue[0]
		return data

	def peek(self):
		return self.queue[0]

	def sizeQueue(self):
		return len(self.queue)


# Queue testing
qe = Queue()
print("Enqueued to queue: {}".format(qe.enqueue(45)))
print("Enqueued to queue: {}".format(qe.enqueue(78)))
print("Enqueued to queue: {}".format(qe.enqueue(21)))
print("Size of Queue: {}".format(qe.sizeQueue()))

print("FIFO Value {}".format(qe.peek()))

print("Popped: {}".format(qe.dequeue()))
print("Popped: {}".format(qe.dequeue()))
print("Size of queue: {}".format(qe.sizeQueue()))

print("FIFO Value {}".format(qe.peek()))
