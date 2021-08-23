s = str(input("enter ur desired text: "))
lowers = 0
uppers = 0

for char in s:
    if char.islower():
        lowers += 1
    if char.isupper():
        uppers += 1

print("uppers: ", uppers, "lowers: ", lowers)

