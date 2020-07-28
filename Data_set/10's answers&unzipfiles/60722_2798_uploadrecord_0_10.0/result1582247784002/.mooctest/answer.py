n = int(input())
a = list(map(int, input().split()))
s = sum(a)
ans = 0
if s % 3 == 0:
    m = s // 3
    s = 0
    c = 0
    ans = 0
    for i in range(n):
        s += a[i]
        if s == m * 2:
            ans += c
        if s == m:
            c += 1
print(ans)
