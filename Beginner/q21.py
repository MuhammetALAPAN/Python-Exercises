import math
movs = [x for x in input("enter robot's movements: ").split(" ")]
x = 0
y = 0
distance = 0
for i in range(0, len(movs)):
    if movs[i] == 'UP':
        x += int(movs[i+1])
    elif movs[i] == 'DOWN':
        x -= int(movs[i+1])
    elif movs[i] == 'RIGHT':
        y += int(movs[i+1])
    elif movs[i] == 'LEFT':
        y -= int(movs[i+1])

distance = math.isqrt(pow(x,2)+pow(y,2))
print("distance from start point: ", distance)