import math
n = int(input())
l = [1]
count = 0
for i in range(2, int(math.sqrt(n))+1):
    l.append(i*i)
length = len(l)
ready = True
while n != 0:
    for i in range(length-1, 0, -1):
        if n % l[i] == 0:
            print(count+n//l[i])
            ready = False
            break
    else:
        length -= 1
        while n >= l[length]:
            n -= l[length]
            count += 1
        del l[length]
        continue
    break
if ready:
    print(count)