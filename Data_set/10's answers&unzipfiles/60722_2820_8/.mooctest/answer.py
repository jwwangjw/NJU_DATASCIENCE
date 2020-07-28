from collections import defaultdict
n = int(input())
d = defaultdict(int)
for i in range(n):
    d[input()] += 1

print(max(d.values()))
