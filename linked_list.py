from structure import Structure

class LinkedList(Structure):
	class __Node:
		def __init__(self, data):
			self.data = data 
			self.next = self.previous = None

	def __init__(self):
		self.__head = self.__tail = None
		self.__currentSize = 0

	def _getHead(self):
		return self.__head

	def isEmpty(self):
		return self.__head == None		

	def append(self, data):
		if data == None:
			return False

		if self.isEmpty():
			self.__head = self.__tail = self.__Node(data)

		else:
			self.__tail.next = self.__Node(data)
			self.__tail.next.previous = self.__tail
			self.__tail = self.__tail.next

		self.__currentSize += 1

	def addFirst(self, data):
		if data == None:
			return False

		if self.isEmpty():
			self.__head = self.__tail = self.__Node(data)

		else:
			self.__head.previous = self.__Node(data)
			self.__head.previous.next = self.__head
			self.__head = self.__head.previous
		
		self.__currentSize += 1	

	def removeFirst(self):
		if self.isEmpty():
			return None

		if self.__head.next == None:
			tmp = self.__head
			self.__head = self.__tail = None

		else:
			tmp = self.__head
			self.__head = self.__head.next
			self.__head.previous = None
		
		self.__currentSize -= 1

		return tmp.data

	def removeLast(self):
		if self.isEmpty():
			return None

		if self.__head.next == None:
			tmp = self.__head
			self.__head = self.__tail = None

		else:
			tmp = self.__tail
			self.__tail = self.__tail.previous
			self.__tail.next = None

		self.__currentSize -= 1

		return tmp.data

	def remove(self, data):
		if self.isEmpty() or data == None:
			return False

		if self.__head.data == data:
			return self.removeFirst()

		if self.__tail.data == data:
			return self.removeLast()

		if self.__currentSize == 2:
			return False

		tmp = self.__head.next 
		while tmp != None:
			if tmp.data == data:
				tmp.previous.next = tmp.next
				self.__currentSize -= 1
				return True
			tmp = tmp.next

		return False

	def removeAll(self):
		self.__init__()

	def find(self, data):
		if self.isEmpty() or data == None:
			return False
		
		if self.__head.data == data or self.__tail.data == data:
			return True

		if self.__currentSize == 2:
			return False

		tmp = self.__head.next
		while tmp != None:
			if tmp.data == data:
				return True
			tmp = tmp.next

		return False

	def replace(self, newElement, oldElement):
		if self.isEmpty() or newElement == None or oldElement == None:
			return False

		if self.__head.data == oldElement:
			self.__head.data = newElement
			return

		if self.__tail.data == oldElement:
			self.__tail.data = newElement
			return

		if self.__currentSize == 2:
			return

		tmp = self.__head.next
		while tmp != None:
			if tmp.data == oldElement:
				tmp.data = newElement
				break
			tmp = tmp.next

	def peekFirst(self):
		return None if self.isEmpty() else self.__head.data

	def peekLast(self):
		return None if self.isEmpty() else self.__tail.data

	def getCurrentSize(self):
		return self.__currentSize

	def getAll(self):
		if self.getCurrentSize() == 0:
			return None

		tmp = self.__head
		while tmp != None:
			yield tmp.data
			tmp = tmp.next
