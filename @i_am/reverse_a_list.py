
newList = [1,2,3,4]





def reverseAListMethod(newList):

		reverseList = []
		for count in range(4):
			reverseList += [newList[len(newList) - count - 1]]
		return reverseList;	


print(reverseAListMethod(newList))

