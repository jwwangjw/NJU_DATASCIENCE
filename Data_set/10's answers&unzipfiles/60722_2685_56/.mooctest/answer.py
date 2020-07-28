import math
T = int(input())
while T > 0:
    N = int(input())
    a = math.floor(N/9)
    b = N%9
    c = b*pow(10, a)
    sum = 0
    for i in range(0, a):
        sum = sum + 9*pow(10, i)
    d = sum + c
    print(d*pow(10, N))
    T-=1