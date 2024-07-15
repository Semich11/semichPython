

for row in range(10):
	for column in range(10):
		if row % 2 == 1:
			print('<', end='')
		else:
			print('>', end='')	
	print()