n = int(input())
a = list(map(int, input().split()))
s = sum(a)
m = 0
c = 0
ans = 0
if s % 3 == 0:
    s //= 3
    for i in range(n-1):
        m += a[i]
        if m == s * 2:
            ans += c
        if m == s:
            c += 1
print(ans)
