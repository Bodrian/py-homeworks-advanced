nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def flat_generator(nested_list):
	for list in nested_list:
		for i in list:
			yield i

for item in flat_generator(nested_list):
	print(item)