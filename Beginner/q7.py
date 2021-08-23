myNumbers = [x for x in input("enter dimension sizes: ").split(",")]
i = int(myNumbers[0])
j = int(myNumbers[1])
myMatrix = [[0 for x in range(j)] for y in range(i)]

for x in range(i):
    for y in range(j):
        myMatrix[x][y] = x*y

print(myMatrix)

#multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

#for row in range(rowNum):
#    for col in range(colNum):
#        multilist[row][col]= row*col

#print(multilist)