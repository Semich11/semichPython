number = int(input("Enter the five digit number"))

last_digit = int(number % 10)

first_digit = int(number / 10000)

fourth_digit = int((number / 10) % 10)

second_digit = int((number / 1000) % 10)

third_digit = int((number / 100) % 10)

print(first_digit,second_digit,third_digit,fourth_digit,last_digit)
