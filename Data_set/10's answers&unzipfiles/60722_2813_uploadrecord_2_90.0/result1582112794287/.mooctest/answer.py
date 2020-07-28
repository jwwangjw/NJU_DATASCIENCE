from collections import defaultdict
n = int(input())
d = defaultdict(int)
a = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    d[name] += score
    a.append((name, score))
m = max(d.values())
dd = defaultdict(int)
for name, score in a:
    if d[name] < m:
        continue
    dd[name] += score
    if dd[name] >= m:
        print(name)
        break
