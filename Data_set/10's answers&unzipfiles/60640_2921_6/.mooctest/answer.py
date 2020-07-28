n, m, d = map(int, input().split())
a = []
for i in range(n):
    a.extend(map(int, input().split()))
a.sort()

n = len(a)
c = 0
j = a[n//2]
for i in a:
    t = abs(i-j)
    if t % d:
        c = -1
        break
    else:
        c += t // d

print(c)
