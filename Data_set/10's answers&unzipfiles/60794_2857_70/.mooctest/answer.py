from math import gcd
n = int(input())
a = list(map(int, input().split()))
d = a[0]
for i in a[1:]:
    d = gcd(d, i)

c = 0
s = int(d ** 0.5)
i = 1
while i <= s:
    if d % i == 0:
        c += 2
    i += 1
if s * s == d:
    c -= 1
print(c)
