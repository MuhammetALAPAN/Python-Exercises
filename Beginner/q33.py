
def myFunc(**kwargs):
    for k, v in kwargs.items():
        print("%d == %d" % (k, v))


myDict = {x: x**2 for x in range(1,4)}
print(myDict)
myFunc(myDict)