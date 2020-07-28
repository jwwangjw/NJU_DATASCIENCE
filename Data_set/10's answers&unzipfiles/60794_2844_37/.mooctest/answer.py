n, t = map(int, input().split())
a = list(map(int, input().split()))
i = 0
j = 0
m = 0
s = 0
while i < n:
    if a[i] + s <= t:
        s += a[i]
        i += 1
        m = max(m, abs(i-j))
    else:
        s -= a[j]
        j += 1
print(m)
