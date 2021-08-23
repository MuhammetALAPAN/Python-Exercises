def testing(number):
    for x in range(0, number+1):
        if x % 7 == 0:
            yield x


n = int(input("enter ur desired value: "))
gen = testing(n)
print(type(gen))
for i in testing(n):
    print(i)


