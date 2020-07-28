n, m = map(int, input().split())
a = list(tuple(map(int, input().split())) for i in range(n))
if sum(i[1] for i in a) > m:
    print(-1)
else:
    c = sorted(i[0] - i[1] for i in a)
    s = sum(i[0] for i in a)
    i = n-1
    while s > m:
        s -= c[i]
        i -= 1
    print(n-i-1)
