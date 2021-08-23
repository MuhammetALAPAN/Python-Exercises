passwords = [x for x in input("enter passwords: ").split(",")]
validPasswords = []
letter = 0
upperletter = 0
number = 0
spechar = 0

for s in passwords:
    if 6 < len(s) < 12:
        for char in s:
            if char.isupper() and char.isalpha():
                upperletter += 1
            elif char.isalpha() and char.islower():
                letter += 1
            elif char.isdigit():
                number += 1
            elif char == '$' or char == '#' or char == '@':
                spechar += 1
            else:
                continue
        if upperletter >= 1 and letter >= 1 and number >= 1 and spechar >= 1:
            validPasswords.append(s)
    upperletter = 0
    letter = 0
    number = 0
    spechar = 0

print(", ".join(validPasswords))

