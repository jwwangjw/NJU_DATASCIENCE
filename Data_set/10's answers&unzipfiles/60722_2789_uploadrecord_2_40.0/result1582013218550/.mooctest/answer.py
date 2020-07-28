t = int(input())
for i in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))[::-1]
    j = 0
    while j < n and j + 1 <= a[j]:
        j += 1
    print(j)
