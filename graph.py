from linkedList import LinkedList

class Graph:
	def __init__(self):
		self.__adj_list = []

	def add_vertex(self, vertex):
		self.__adj_list.append(LinkedList())
		self.__adj_list[-1].append(vertex)

	def add_edge(self, ver1, ver2, dircted = False):
		if len(self.__adj_list) <= 1:
			return None

		for vertex in self.__adj_list:
			if vertex.peekFirst() == ver1:
				vertex.append(ver2)

			if vertex.peekFirst() == ver2 and not dircted:
				vertex.append(ver1)

	def remove_vertext(self, vertex):
		if len(self.__adj_list) == 0:
			return None

		for i in range(0, len(self.__adj_list)):
			if self.__adj_list[i].peekFirst() == vertex:

				for _ in range(0, self.__adj_list[i].getCurrentSize()):
					tmpVar = self.__adj_list[i].removeLast() 
					for ver in self.__adj_list:
						if ver.peekFirst() == tmpVar:
							ver.remove(vertex)

				del(self.__adj_list[i])
				return True			

	def remove_edge(self, ver1, ver2, dircted = False):
		if len(self.__adj_list) <= 1:
			return None

		for vertex in self.__adj_list:
			if vertex.peekFirst() == ver1:
				vertex.remove(ver2)

			if vertex.peekFirst() == ver2 and not dircted:
				vertex.remove(ver1)

	def number_of_vertices(self):
		return len(self.__adj_list)

	def remove_all(self):
		self.__adj_list = []

	def get_all_vertices(self, vertex):
		for ver in self.__adj_list:
			yield ver.peekFirst()

	def find(self, vertex):
		for ver in self.__adj_list:
			if ver.peekFirst() == vertex:
				return ver

	def get_first(self):
		return self.__adj_list[0]
