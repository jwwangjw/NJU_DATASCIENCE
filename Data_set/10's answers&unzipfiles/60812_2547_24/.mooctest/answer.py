import itertools
import numpy
def zero(n,k,a):
    b = {}
    a = list(itertools.combinations(a, 2))  
    for i in a:
        x = abs(numpy.diff(i))
        sorted(i)
        if x ==k and  i not in b:
            b[i] =1
    print(len(b))
        
for i in range(int(input())):      
    n = int(input())
    a = list(map(int,input().rstrip().split()))
    k =int(input())
    r = zero(n,k,a)