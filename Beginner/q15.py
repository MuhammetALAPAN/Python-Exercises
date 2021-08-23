num = input("enter ur desired value: ")

numList = []

numList.append(num)
numList.append(num + num)
numList.append(num + num + num)
numList.append(num + num + num + num)

sum = 0

for x in numList:
    sum += int(x)

print("result: ", sum)