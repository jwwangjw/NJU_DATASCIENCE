from collections import defaultdict
n = int(input())
x = defaultdict(int)
y = defaultdict(int)
xy = defaultdict(int)
c = 0
for i in range(n):
    xi, yi = map(int, input().split())
    c += x[xi] + y[yi] - xy[(xi, yi)]
    x[xi] += 1
    y[yi] += 1
    xy[(xi, yi)] += 1

print(c)
