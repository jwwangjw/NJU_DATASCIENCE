n, d = map(int, input().split())
n = n + n - d
for i in range(int(input())):
    x, y = map(int, input().split())
    t = x + y >= d and x + y <= n and x - y <= d and y - x <= d
    print("YES" if t else "NO")
