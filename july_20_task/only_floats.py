
def only_floats(number, negative):

	if type(number) == float and type(negative) == float:
		return 2
	elif type(number) == float or type(negative) == float:
		return 1
	else: return 0




print(only_floats(2,1))