

def sequenceOfStringToList():
    # con_input = input("Enter a comma-separated list of numbers: ")
    con_input = "34,67,55,33,12,98"


    splitString = con_input.split(",")
    stringToList = list (splitString)
    stringToTuple = tuple(stringToList)

    listToString = str(stringToList)
    tupleToString = str(stringToTuple)
    print(listToString + tupleToString)
    returnString = listToString + tupleToString


    # print(splitString)
    # print(stringToList, " ", stringToTuple)
    return returnString


print(sequenceOfStringToList())

arr  = [1,3]
stri = str(arr)
print(stri)
tup = (1,2)
print(stri + str(tup))

greet = """welcome
to
Semicolon
"""

print(greet)
print(greet.splitlines())

