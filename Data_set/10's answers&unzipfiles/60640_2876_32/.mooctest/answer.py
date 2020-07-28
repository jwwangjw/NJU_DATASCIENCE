n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(1, n-1):
    if a[i-1] and not a[i] and a[i+1]:
        a[i+1] = 0
        c += 1
print(c)
