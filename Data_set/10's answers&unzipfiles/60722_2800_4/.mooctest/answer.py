n, d = map(int, input().split())
a = list(map(int, input().split()))
m = 0
for i in range(1, n):
    if a[i] <= a[i-1]:
        x = (a[i-1] - a[i]) // d + 1
        a[i] += x * d
        m += x

print(m)
