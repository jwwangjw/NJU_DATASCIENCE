v = int(input())
a = list(map(int, input().split()))
m = min(a)
if v < m:
    print(-1)
else:
    a = [0] + a
    d = [0] * 10
    k = 9 - a[::-1].index(m)
    n = v // m
    d[k] = n
    v -= n * m
    for i in range(0, n):
        for j in range(9, k, -1):
            if v >= a[j]-a[k]:
                v -= a[j] - m
                d[j] += 1
                d[k] -= 1
                break
        if v <= 0:
            break
    for i in range(9, k-1, -1):
        print(str(i)*d[i], end='')
    print()
