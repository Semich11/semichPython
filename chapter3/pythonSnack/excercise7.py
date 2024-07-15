

print(f"{'number':>6} {'square':>6} {'cube':>6}")
for number in range(0, 6):
	square = number * number
	cube = number * number * number
	print(f"{number:>6} {square:>6} {cube:>6}")