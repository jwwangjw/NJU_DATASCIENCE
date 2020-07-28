evens = []
n = 1
mx = 10**5
while n <= mx:
    evens.append(n)
    n *= 2
    evens.append(n)
    n *= 2
    n += 1
    
from bisect import bisect_right


#print(allprimes)
testCases = int(input().strip())
while testCases > 0:
    testCases -= 1
    n = int(input().strip())
    i = bisect_right(evens, n)
    print(' '.join(map(str, evens[:i])))