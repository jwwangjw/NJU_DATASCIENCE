n, x = map(int, input().split())
s = 0
for i in sorted(map(int, input().split())):
    s += i * x
    x = max(1, x-1)
print(s)
