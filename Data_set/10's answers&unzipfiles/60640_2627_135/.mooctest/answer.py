from math import sqrt

for _ in range(int(input())):
    p,s = tuple(map(float, input().strip().split()))
    
    temp = sqrt(p*p - 24*s)
    
    v = pow((p-temp)/12, 2)*(p/4 - 2*(p-temp)/12)
    
    print("{0:.5f}".format(v))