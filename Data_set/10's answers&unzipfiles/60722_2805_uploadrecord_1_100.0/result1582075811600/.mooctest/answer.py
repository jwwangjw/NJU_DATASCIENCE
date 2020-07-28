n = int(input())
a = list(map(int, input().split()))
c = 1
m = 1
for i in range(1, n):
    if a[i] - a[i-1] > 0:
        c += 1
        m = max(m, c)
    else:
        c = 1
print(m)
