


number = 321




str_temp = ""
print(str_temp)


while number > 0:
	temp  = number % 10
	str_temp += str(temp)
	number // 10

for character in str_temp:
	for digit in str_temp:
		if character > digit:
			temp = character
			character = digit
			digit = temp"""

#print("str_temp")

	