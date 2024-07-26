


print(f"{"a":>4}{"b":>4}{"a**b":>8}")
b = 2
for a in range(1, 6):
	print(f"{a:>4}{b:>4}{a**b:>8}")
	b += 1