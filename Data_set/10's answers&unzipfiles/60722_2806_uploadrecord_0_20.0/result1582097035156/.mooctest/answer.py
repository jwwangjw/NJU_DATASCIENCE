n = int(input())
p = 1000
s = 0
for i in range(n):
    x, y = map(int, input().split())
    p = min(p, y)
    s += x * p
print(s)
