import math
n = int(input())
a = int(input())
b = int(input())
c = int(input())
gcd_ab = math.gcd(a, b)
gcd_bc = math.gcd(b, c)
gcd_ac = math.gcd(a, c)
lcm_ab = int(a*b//gcd_ab)
lcm_bc = int(b*c//gcd_bc)
lcm_ac = int(a*c//gcd_ac)
lcm_abc = int(a*lcm_bc//math.gcd(a, lcm_bc))
low = min(a, b, c)
high = low*n
mid = 0
while low < high:
    mid = low + (high-low)//2
    num = mid//a + mid//b + mid//c - mid//lcm_ab - mid//lcm_ac - mid//lcm_bc + mid//lcm_abc
    if num < n:
        low = mid+1
    else:
        high = mid
print(low)
