nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class Mylist:
	def __init__(self, nested_list):
		self.nested_list = nested_list

	def __iter__(self):
		i = 0
		list = []
		while i != len(nested_list):
			list += nested_list[i]
			i += 1
		return list

	def __next__(self, list):
		if len(list) == 0:
			raise StopIteration
		return list.pop()



for item in Mylist(nested_list):
	print(item)

#flat_list = [item for item in Myrange(nested_list)]