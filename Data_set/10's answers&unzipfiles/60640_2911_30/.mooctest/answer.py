n, m = map(int, input().split())
c = [0] + list(map(int, input().split()))

if c[1] == 0 and c.count(0) == n+1:
    print(0)
else:
    f = [i for i in range(n+10)]

    def find(x):
        if x == f[x]:
            return x
        f[x] = find(f[x])
        return f[x]

    for i in range(m):
        x, y = map(int, input().split())
        xx = find(x)
        yy = find(y)
        if xx != yy:
            f[xx] = yy
            c[yy] = min(c[xx], c[yy])

    print(sum(c[i] for i in range(1, n+1) if i == find(i)))
