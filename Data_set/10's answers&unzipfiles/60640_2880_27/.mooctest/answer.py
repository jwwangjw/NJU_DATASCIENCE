n, k = map(int, input().split())
a = list(map(int, input().split()))
l, r = 0, n - 1
while l < n and a[l] <= k:
    l += 1
while r > l and a[r] <= k:
    r -= 1
print(n - r + l - 1)
