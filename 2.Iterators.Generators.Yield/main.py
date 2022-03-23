nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class Mylist:
	def __init__(self, nested_list):
		self.nested_list = nested_list

	def __iter__(self):
		return self

	def __next__(self):
		if len(nested_list) == 0:
			raise StopIteration
		return nested_list.pop()



for item in Mylist(nested_list):
	print(item)

#flat_list = [item for item in Myrange(nested_list)]