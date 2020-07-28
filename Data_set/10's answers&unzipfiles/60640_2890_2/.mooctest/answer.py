n, x0, y0 = map(int, input().split())
s = set()
c = 0
for i in range(n):
    x, y = map(int, input().split())
    if x != x0:
        s.add((y-y0)/(x-x0))
    else:
        c = 1
print(len(s) + c)
