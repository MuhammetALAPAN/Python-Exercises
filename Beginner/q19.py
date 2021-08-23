#data = [tuple(x.split(",")) for x in input("enter data: ").split(" ")]
#print(data)
#import operator
#data.sort(key=operator.itemgetter(0,1,2))
#print(data)
import operator

l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print(sorted(l, key=operator.itemgetter(0,1,2)))