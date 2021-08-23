"""
print("please enter desired factorial number:")

givenNumber = int(input())

givenNumber = range(1, givenNumber + 1)

result = 1

for n in givenNumber:
    result *= n

print(result)
"""

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

print("please enter desired factorial number:")
x = int(input())
print(fact(x))