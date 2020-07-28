from functools import reduce
T = int(input())
for i in range(T):
    n = int(input())
    print(n*reduce(lambda x, y: x+y, [i for i in range(2, 2*n+1) if i % 2 == 1 or i == 2]))