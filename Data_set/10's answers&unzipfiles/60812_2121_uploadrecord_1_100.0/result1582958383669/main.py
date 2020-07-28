from functools import reduce
n = int(input())
if n != 0:
    count = 10
    for i in range(1, n):
        count += 9*reduce(lambda x, y: x*y, range(10-i, 10))
    print(count)
else:
    print(1)