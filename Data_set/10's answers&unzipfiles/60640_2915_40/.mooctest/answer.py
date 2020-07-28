n = int(input())
a = list(map(int, input().split()))
m = 1
c = 1
for i in range(1, n):
    if a[i] <= a[i-1] * 2:
        c += 1
    else:
        m = max(m, c)
        c = 1
print(max(m, c))
