class node():

	def __init__(self,data):
		self.data = data
		self.next = None

class linkedlist():

	def __init__(self):
		self.head = None

	def printlist(self):
		temp = self.head
		while (temp):
			print (temp.data)
			temp = temp.next



if __name__ == '__main__':
	
	linklist1 = linkedlist()
	linklist1.head = node(1)
	two = node(2)
	three = node(3)
	linklist1.head.next = two
	two.next = three
	linklist1.printlist()

