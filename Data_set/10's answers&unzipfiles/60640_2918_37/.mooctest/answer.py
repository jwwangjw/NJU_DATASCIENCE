n = int(input())
a = sorted(map(int, input().split()))
c = 0
for i in range(n):
    if (a[i]+1) * c <= i:
        c += 1
print(c)
