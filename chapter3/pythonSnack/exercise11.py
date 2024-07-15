

while True:
	gallons = int(input("Enter gallon used (-1 to end): "))

	if gallons == -1:

		break

	miles = int(input("Enter miles driven: "))

	milage = miles/gallons
	print(f"The miles/gallons for this tank was {milage: .6f} ")