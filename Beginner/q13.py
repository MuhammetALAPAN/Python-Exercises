s = str(input("enter ur desired text: "))
letters = 0
digits = 0

for char in s:
    if char.isdigit():
        digits = digits + 1
    if char.isalpha():
        letters = letters + 1

print("letters: ", letters, "digits: ", digits)

