n = int(input())
m = 0
d = 0
for i, p in enumerate(map(int, input().split()), 1):
    m = max(m, p)
    if i == m:
        d += 1

print(d)
