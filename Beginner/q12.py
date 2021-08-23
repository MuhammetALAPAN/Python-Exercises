""""

resultList = []
for x in range(1000, 3001):
    tempList = list(str(x))
    isAllDigitsDivisibleToTwo = 1
    for y in tempList:
        if int(y) % 2 != 0:
            isAllDigitsDivisibleToTwo = 0
            break
    if isAllDigitsDivisibleToTwo == 1:
        resultList.append(x)


print(", " .join(str(resultList)))


"""


values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))