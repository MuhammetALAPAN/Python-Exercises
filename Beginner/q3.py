x = int(input())

#myDict = {}
myDict = dict()

integralNumber = range(x)

for x in integralNumber:
    myDict[x + 1] = (x + 1) * (x + 1)

print(myDict)