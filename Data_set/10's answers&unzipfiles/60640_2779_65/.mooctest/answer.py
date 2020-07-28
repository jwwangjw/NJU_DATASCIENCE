
import math

T = int(input().strip())

while T > 0:
    T -= 1
    #st = list(filter(lambda c: c.isalpha(),list(input().strip())))
    l = int(input().strip())
    array = list(map(int, input().strip().split()))
    #num1, num2 = (list(map(int, input().strip().split())))

    mn = min(array)
    mx = max(array)
    print(mn // math.gcd(mn,mx) * mx)
    