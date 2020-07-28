n = int(input())
a = list(map(int, input().split()))
m = 101
for i in range(min(a), max(a)+1):
    d = 0
    for j in a:
        if j != i:
            d = abs(j-i)
            break
    for j in a:
        if j != i and abs(j-i) != d:
            break
    else:
        m = min(m, d)

print(-1 if m == 101 else m)
