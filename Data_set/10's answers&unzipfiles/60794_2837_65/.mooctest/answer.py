n, l, r = map(int, input().split())
mn = n - l + 2 ** l - 1
mx = 2 ** (r-1) * (n - r + 2) - 1
print(mn, mx)
