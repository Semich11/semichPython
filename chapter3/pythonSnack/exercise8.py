
numbers = [0,0,0,0]

sum = 0;
product = 1;

for count in range(4):

	numbers[count] = int(input("Enter first number"))
	sum += numbers[count]
	product *= numbers[count]



size = len(numbers)

index = 0

for count in numbers:
	innerIndex = 0
	for swap in numbers:
		if numbers[index] > numbers[innerIndex]:
			holder = numbers[index]
			numbers[index] = numbers[innerIndex]
			numbers[innerIndex] = holder

		innerIndex += 1

	index += 1

print("Largest number: ",numbers[0])
print("Smallest number: ",numbers[size - 1])

print("product: ",product)

print(sum)
print("Average: ",sum / size)

