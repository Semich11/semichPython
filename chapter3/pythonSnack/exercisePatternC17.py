increment = 0
for pattern in range(11, 0, -1):
	for space in range(increment):
		print(" ",end=" ")
	for star in range(pattern):
		print("*", end=" ")
	print()
	increment += 1