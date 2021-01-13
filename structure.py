'''this is abstract class, all other classes should inherit it''' 

from abc import ABC, abstractmethod

class Structure(ABC):

	@abstractmethod
	def remove(self, element):
		pass

	@abstractmethod
	def removeAll(self):
		pass

	@abstractmethod
	def isEmpty(self):
		pass

	@abstractmethod
	def find(self, element):
		pass

	@abstractmethod
	def replace(self, newElement, oldElement):
		pass
