n = int(input())
x = [False] * (n + 1)
y = [False] * (n + 1)
a = []
for i in range(1, n**2+1):
    h, v = map(int, input().split())
    if not x[h] and not y[v]:
        a.append(i)
        x[h] = True
        y[v] = True
print(*a)
