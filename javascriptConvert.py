userInput = [1,2,3,4,5]

def someSum(userInput):

    summation = 0

    outPut = []


    count = 0

    global i

    for i in userInput:
        summation += i

        count += 1
        if count == 2:
            count = 0
            outPut.append(summation)
            summation = 0



    array_length = len(userInput)

    if array_length % 2 > 0:
        outPut.append(i)
    return outPut


print(someSum(userInput))