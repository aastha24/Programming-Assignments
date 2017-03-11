class Queue():
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return (self.items ==[])

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def print_myq(self):
		print (self.items)

q=Queue()
q.enqueue(32)
q.enqueue('God')
q.enqueue(45.0)

q.print_myq()
q.dequeue()
q.print_myq()
