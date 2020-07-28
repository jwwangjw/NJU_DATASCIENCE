n = int(input())
a = list(map(int, input().split()))
i, j = a.index(1) + 1, a.index(n) + 1
if abs(i-j) == n-1:
    print(n-1)
else:
    print(max(n-i, i-1, n-j, j-1))
