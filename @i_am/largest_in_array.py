femiArray = [1, 2, 3, 100, 5, 6, 7, 8, 9, 10]


def largestNumberInArray(newArray):
		
	highest = 0;
	for number in newArray:
		if number > highest:
			highest = number;

	return highest;

print(largestNumberInArray(femiArray));
