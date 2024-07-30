
Step 01: create a variable that will hold string.
Step 02: use for loop to loop through all the range of numbers
Step 03: for each number gotten from the loop, convert the number to string
Step 04: use a for loop to loop the amount of the length of the string in Step 02
Step 05: collect element from the string variable and convert it to integer
Step 06: add the integer gotten from Step 05: to the variable declare in Step 01
Step 07: convert the variable in Step 01 to integer
Step 08: if the integer gotten in step 05 is greater than 0 break the loop, else back to Step04.

once Step 04 loop is done continue. 

Step 09: check if the integer in Step 06 modulo 2 is greater 0, print number ending with ","





tempHolder = ""



for number in range(1000, 3001):
	str_number = str(number)
	for _ in range(len(str_number)):
		parse_to_int = int(str_number[_])
		tempHolder += str(parse_to_int)
		all_to_int = int(tempHolder)
		if parse_to_int % 2 > 0:
			break;
	if all_to_int % 2 == 0:	
		print(number, end=", ")





	
