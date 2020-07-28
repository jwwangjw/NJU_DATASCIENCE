import math
n = int(input())
m = int(input())
p = int(input())
for i in range(1, n):
    if math.pow(i, p//m) >= n:
        print(i-1)
        break