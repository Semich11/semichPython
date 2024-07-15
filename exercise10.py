firstvalue = int(input("Enter first number: "))
secondvalue = int(input("Enter second number: "))
thirdvalue = int(input("Enter third number: "))

sum = firstvalue + secondvalue + thirdvalue
print("The sum of the numbers is ",sum)

average = sum/3
print("The average of the numbers is ",average)

product = firstvalue * secondvalue * thirdvalue
print("The product of the numbers is ",product)

if firstvalue > secondvalue and firstvalue > thirdvalue:
	print(firstvalue, "is the largest number")
elif secondvalue > firstvalue and secondvalue > thirdvalue:
	print(secondvalue, "is the largest number")
elif thirdvalue > firstvalue and thirdvalue > secondvalue:
	print(thirdvalue, "is the largest number")

if firstvalue < secondvalue and firstvalue < thirdvalue:
	print(firstvalue, "is the smallest number")
elif secondvalue < firstvalue and secondvalue < thirdvalue:
	print(secondvalue, "is the smallest number")
elif thirdvalue < firstvalue and thirdvalue < secondvalue:
	print(thirdvalue, "is the smallest number")