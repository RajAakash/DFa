class ListNode: 

		def __init__(self, data): 
			self.data = data 
			self.next = None

class BinaryTreeNode: 

	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

class Conversion: 

	def __init__(self, data = None): 
		self.head = None
		self.root = None

	def push(self, new_data): 

		new_node = ListNode(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	def convertList2Binary(self): 
		q = [] 

		if self.head is None: 
			self.root = None
			return

		self.root = BinaryTreeNode(self.head.data) 
		q.append(self.root) 


		self.head = self.head.next

		while(self.head): 

			parent = q.pop(0) 

			leftChild= None
			rightChild = None

			leftChild = BinaryTreeNode(self.head.data) 
			q.append(leftChild) 
			self.head = self.head.next
			if(self.head): 
				rightChild = BinaryTreeNode(self.head.data) 
				q.append(rightChild) 
				self.head = self.head.next

			parent.left = leftChild 
			parent.right = rightChild 

	def Traversal(self, root): 
		if(root): 
			self.Traversal(root.left) 
			print (root.data), 
			self.Traversal(root.right) 

conv = Conversion() 
conv.push('a')
conv.push('b') 
conv.push('c') 
conv.push('d') 
conv.push('e') 
conv.push('f') 

conv.convertList2Binary() 

print ("Binary Tree:")
print("Root node first")
conv.Traversal(conv.root) 


