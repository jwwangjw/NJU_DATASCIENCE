n = int(input())
a = list(map(int, input().split()))
s = [0, 0]
i, j = 0, n-1
c = 1
while i <= j:
    if a[i] > a[j]:
        s[c % 2] += a[i]
        i += 1
    else:
        s[c % 2] += a[j]
        j -= 1
    c += 1
print(s[1], s[0])
