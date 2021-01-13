from structure import Structure
from linkedList import LinkedList

class HashMap(Structure):
	def __init__(self):
		self.__entrySize = 0
		self.__hashArraySize = 50
		self.__hashArray = [LinkedList() for i in range(0, self.__hashArraySize)]

	def add(self, key, value):
		hashCode = self.__hashFunction(key)
		self.__hashArray[hashCode].append((key, value))
		self.__entrySize += 1

		if self.loadFactor() > 0.85:
			print(self.__hashArraySize, self.loadFactor(), key)
			self.__getNewSize()
			print(self.__hashArraySize, self.loadFactor())

	def __hashFunction(self, key):
		if type(key) == int or type(key) == float:
			return int(key) % self.__hashArraySize

		if type(key) == str:
			return key.__hash__() % self.__hashArraySize

		raise TypeError(" unhashable type {}".format(type(key)))

	def loadFactor(self):
		return self.__entrySize / self.__hashArraySize

	def __getNewSize(self):
		self.__hashArraySize *= 3 
		self.__entrySize = 0
		arr = self.__hashArray
		self.__hashArray = [LinkedList() for i in range(0, self.__hashArraySize)]

		for i in range(len(arr)):
			tmp = arr[i]._getHead()
			if tmp == None:
				continue

			while tmp != None:
				self.add(tmp.data[0], tmp.data[1])
				tmp = tmp.next

	def __findValueByKey(self, linkedList, key, flag = False):		
		tmp = linkedList._getHead()
		if tmp == None:
			return False

		if tmp.data[0] == key and flag:
			linkedList.removeAll()
			self.__entrySize -= 1
			return True

		if tmp.data[0] == key:
			return True

		tmp = tmp.next

		while tmp != None:
			if tmp.data[0] == key and flag:
				linkedList.remove(tmp.data)
				return True

			if tmp.data[0] == key:
				return True

			tmp = tmp.next

		return False		

	def find(self, key):
		hashCode = self.__hashFunction(key)
		return self.__findValueByKey(self.__hashArray[hashCode], key)

	def remove(self, key):
		hashCode = self.__hashFunction(key)
		return self.__findValueByKey(self.__hashArray[hashCode], key, flag = True)			

	def removeAll(self):
		self.__init__()

	def isEmpty(self):
		return self.__entrySize == 0

	def replace(self):
		pass
