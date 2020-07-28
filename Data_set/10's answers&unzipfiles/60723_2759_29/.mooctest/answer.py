import math

def numinrange(m,n,a):
    s = n//a - m//a
    if m%a == 0:
        s += 1
    return s

for t in range(int(input())):
    m, n, a, b = [int(i) for i in input().split()]
    print(numinrange(m,n,a) + numinrange(m,n,b) - numinrange(m,n,a*b//math.gcd(a,b)))