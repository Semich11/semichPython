userInput = int(input("Type 1 to deposit 2 to withdraw or -1 to check balance: "))

balance = 0;

while userInput != -1:



	if userInput == 1:
		deposit = int(input("Deposit amount: "))
		balance += deposit

	elif userInput == 2:
		withdraw = int(input("Withdrawal amount: "))
		balance -= withdraw

	else:
		print("Invalid input.")



	userInput = int(input("Type 1 to deposit 2 to withdraw or -1 to check balance: "))



print(balance)
