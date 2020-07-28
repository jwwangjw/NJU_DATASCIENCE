n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0
e = [False] * (n+1)
j = 0
for i in range(n):
    while e[a[j]]:
        j += 1
    if a[j] == b[i]:
        j += 1
    else:
        c += 1
        e[b[i]] = True

print(c)
