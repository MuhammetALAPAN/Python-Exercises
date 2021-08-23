
s = [x for x in input("enter ur account details: ").split()]
d = 0
w = 0
sum = 0
for x in s:
    if x == 'D':
        d = 1
    elif x == 'W':
        w = 1
    elif d == 1:
        sum += int(x)
        d = 0
    elif w == 1:
        sum -= int(x)
        w = 0
print(sum)

