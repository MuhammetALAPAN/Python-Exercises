
numbersList = []

x = range(2000, 3200)

for i in x:
    if i % 10 != 0 and i % 5 != 0 and i % 7 == 0:
        numbersList.append(str(i))

for n in numbersList:
    print(n, end=", ")

print(','.join(numbersList))
