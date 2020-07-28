n, r, avg = map(int, input().split())
t = n * avg
e = []
for i in range(n):
    a, b = map(int, input().split())
    t -= a
    if a != r:
        e.append((a, b))

e.sort(key=lambda x: x[1])
s = 0
for a, b in e:
    if t <= 0:
        break
    c = min(t, r-a)
    t -= c
    s += c * b

print(s)
