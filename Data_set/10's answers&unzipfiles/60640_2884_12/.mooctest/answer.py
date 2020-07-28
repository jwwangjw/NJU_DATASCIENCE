n, d = map(int, input().split())
a = sorted(map(int, input().split()))
c = 0
for i in range(n-1):
    for j in range(i+1, n):
        if a[j] - a[i] <= d:
            c += 2
        else:
            break
print(c)
