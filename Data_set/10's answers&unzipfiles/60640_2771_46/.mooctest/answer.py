import math
for _ in range(int(input())):
    x=math.sqrt(int(input()))
    if math.floor(x)==x:
        print(1)
    else:
        print(0)