from random import randint


answer = [13, 8, 24, 5, 15, 9, 21, 6, 19, 7]


a = "Question: 1. 8 + 5 = ?: "

b = "Question: 2. 15 - 7 = ?: "

c = "Question: 3. 6 × 4 = ?: "

d = "Question: 4. 20 ÷ 4 = ?: "

e = "Question: 5. 9 + 6 = ?: "

f = "Question: 6. 14 - 5 = ?: "

g = "Question: 7. 7 × 3 = ?: "

h = "Question: 8. 18 ÷ 3 = ?: "

i = "Question: 9. 12 + 7 = ?: "

j = "Question: 10. 10 - 3 = ?: "


question = [a, b, c, d, e, f, g, h, i, j]




count = 1
innerCount = 1
correct = 0

while count <= 10:
	guessNumber = randint(0, 10)

	print(f"Question: {count}.",question[guessNumber])
	print(answer[guessNumber])

	userInput = int(input("100. Guess a number: "))
	while innerCount <= 10:
		if userInput == answer[guessNumber]:
			print("correct")
			correct += 1
			break;
		else: 
			print("incorrect")
			print("innerCount: ",innerCount)
			innerCount += 1
			userInput = int(input("Guess a number: "))

	count += 1


print("Final score: ",correct)






#print(question[0])



#for attempt in range(3):
	#userInput = int(input(question[guessNumber]))








