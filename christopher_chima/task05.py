# Step01 collect integer between 0 and 1000
# Step02 create a variable and assign it to 0
# Step03 continue Step04 - Step07 until number is equal than 0.

# Step04 extract the last digit from the integer
# Step05 add the extracted digit to sum
# Step06 remove the extracted digit from the integer
# Step07 go back to Step03.

number = int(input("Input number between 0 and 1000: "))

sum = 0
while number > 0:
	temp_holder = number % 10
	sum += temp_holder
	number //= 10

print("Palin: ", sum)