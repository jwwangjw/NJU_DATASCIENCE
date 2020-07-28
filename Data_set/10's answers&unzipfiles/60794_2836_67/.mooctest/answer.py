n = int(input())
a = list(map(int, input().split()))
i = 1
while i < n and a[i-1] <= a[i]:
    i += 1
if i == n:
    print(0)
else:
    j = i + 1
    while j < n and a[j-1] <= a[j]:
        j += 1
    if j < n or a[-1] > a[0]:
        print(-1)
    else:
        print(j-i)
