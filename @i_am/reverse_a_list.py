
newList = [1,2,3,4]





def reverseAListMethod(newList):

		reverseList = []
		for count in range(len(newList)):
			reverseList += [newList[len(newList) - count - 1]]
		return reverseList;	


print(reverseAListMethod(newList))



newList = [1,2,3,4]


otherList = [5,6,7,8]
for count in range(len(newList)):
	otherList += [newList[count]
print(otherList)
