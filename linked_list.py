class node():

	def __init__(self,data):
		self.data = data
		self.next = None

class linkedlist():

	def __init__(self):
		self.head = None

	#Add a new node at beginning
	def push_data(self,new_data):
		new_node = node(new_data)
		new_node.next = self.head
		self.head = new_node

	#Add a new node at end
	def push_data_at_end(self,new_data):
		new_node = node(new_data)

		#check for linked list being empty
		if self.head is None:
			self.head = new_node
			return

		last = self.head
		while (last.next):
			last = last.next

		last.next = new_node

	#Add a new node at given a given position
	def push_data_at_pos(self,prev_node,new_data):


		if prev_node is None:
			print("Incorrect Previous node")
			return
		new_node = node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node


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
	print("First linked list is:")
	linklist1.printlist()
	linklist1.push_data(0)
	print("linked list after insertion in beginning:")
	linklist1.printlist()
	linklist1.push_data_at_end(4)
	print("linked list after insertion at end:")
	linklist1.printlist()
	linklist1.push_data_at_pos(linklist1.head.next,3)
	print("linked list after insertion at given position:")	
	linklist1.printlist()

