
number1 = 0;
number2 = 0;

flag = True

while flag:
	number1 = int(input('Enter first integer: '))

	if number1 == 1:
		flag = False
	elif number1 == 2:
		flag = False

	number2 = int(input('Enter second integer: '))
	if number2 == 1:
		flag = False
	elif number2 == 2:
		flag = False
total = number1 + number2
print( )
