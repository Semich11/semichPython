


def biggest_odd_number(number):

	index = 0
	highest_odd = 0

	for digit in number:
		temp_store = int(digit)

		if temp_store % 2 > 0 and temp_store > highest_odd:
			highest_odd = temp_store

	return highest_odd

print(biggest_odd_number("23569"))

	