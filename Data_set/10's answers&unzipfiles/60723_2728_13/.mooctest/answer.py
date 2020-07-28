from itertools import combinations
from functools import reduce


for t in range(int(input())):
    input()
    a = [int(i) for i in input().split()]
    b = [(j-i)*min(a[i],a[j]) for i,j in combinations(range(len(a)),2)]
    print(reduce(max, b))
    