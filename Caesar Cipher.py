
text = [x for x in input("Enter the text to be encrypted: ")]

for i in range(len(text)):
    unicode = ord(text[i])  # Assigning current letter's ASCII value to a parameter.
    char = text[i]
    if str.islower(char) and unicode + 7 >= 123:  # checking lowercase character ASCII value overflow
        text[i] = chr(97 + (unicode + 7 - 123))
    elif str.isupper(char) and unicode + 7 >= 90:  # checking uppercase character ASCII value overflow
        text[i] = chr(65 + (unicode + 7 - 90))
    elif str.islower(char) or str.isupper(
            char):  # checking lowercase and uppercase condition for applying statement only to letters.
        text[i] = chr(unicode + 7)

print("Encoded Text: " + "".join(text))
