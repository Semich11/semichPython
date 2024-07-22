

import math

def divide_or_square(number):
	if number % 5 == 0:	
		root = math.sqrt(number)
		return f"{root:.2f}"

	else: return number % 5

print(divide_or_square(13))