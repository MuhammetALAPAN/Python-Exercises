binaryList = [x for x in input("Enter binary numbers: ").split(",")]
isDivisibleFive= []
for x in binaryList:
    if int(x, 2) % 5 == 0:
        isDivisibleFive.append(x)

print(", " .join(isDivisibleFive))
