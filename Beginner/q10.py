myString = [x for x in input("enter ur desired text: ").split(" ")]
#myString = list(dict.fromkeys(myString))
#myString.sort()
print(", ".join(list(sorted(set(myString)))))
