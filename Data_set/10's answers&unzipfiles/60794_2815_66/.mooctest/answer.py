n = int(input())
a = list(map(int, input().split()))
n, z = 0, 0
s = sum(map(abs, a)) - len(a)
for i in a:
    if i < 0:
        n += 1
    elif i == 0:
        z += 1

s += z * 2

if z == 0 and n % 2:
    s += 2

print(s)
