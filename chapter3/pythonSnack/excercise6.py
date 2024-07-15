
userInput = input("Have you have this problem before (Yes or no)?: ").strip().lower()

if userInput == "yes":
	print("Well, you have it again")
elif userInput == "no":
	print("Well, you have it now")