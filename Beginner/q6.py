import math

C = 50
H = 30


def myCalc(myList):
    myResultList = []
    for x in myList:
        result = round(math.sqrt((2 * C * int(x)) / H))
        myResultList.append(result)
    return myResultList


x = input("enter ur sequence of numbers")

splittedInput = x.split(",")

myResultList = myCalc(splittedInput)

print(myResultList)