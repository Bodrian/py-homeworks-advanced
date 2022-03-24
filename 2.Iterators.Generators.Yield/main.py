nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class Mylist:
	def __init__(self, nested_list):
		self.nested_list = nested_list
		self.list = []
		self.i = 0

	def __iter__(self):
		return self

	def __next__(self):
		while self.i != len(nested_list):
			self.list += nested_list[self.i]
			self.i += 1
		if len(self.list) == 0:
			raise StopIteration
		return self.list.pop(0)



for item in Mylist(nested_list):
	print(item)

flat_list = [item for item in Mylist(nested_list)]
print(flat_list)
