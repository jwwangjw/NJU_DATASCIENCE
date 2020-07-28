from collections import defaultdict
n, m = map(int, input().split())
a = [defaultdict(int) for i in range(m)]
for i in range(n):
    for j, x in enumerate(input()):
        a[j][x] += 1
s = 0
for i, x in enumerate(map(int, input().split())):
    s += x * max(a[i].values())
print(s)
