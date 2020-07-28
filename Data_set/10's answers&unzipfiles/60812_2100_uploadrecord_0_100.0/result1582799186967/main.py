from functools import reduce
n = reduce(lambda x, y: x*y, range(1, int(input())+1))
a = b = 0
while n % 2 == 0:
    n /= 2
    a += 1
while n % 5 == 0:
    n /= 5
    b += 1
print(min(a, b))