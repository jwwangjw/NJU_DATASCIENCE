n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

v = [False] * n


def f(x):
    for i in range(n):
        if v[i]:
            continue
        if a[i][0] == a[x][0] or a[i][1] == a[x][1]:
            v[i] = True
            f(i)


c = 0
for i in range(n):
    if v[i]:
        continue
    v[i] = True
    c += 1
    f(i)

print(c-1)
