n = int(input())
a = list(map(int, input().split()))
try:
    p = a.index(1)
    c = 1
    z = 1
    for i in a[p+1:]:
        if i == 1:
            c *= z
            z = 1
        else:
            z += 1
    print(c)
except ValueError:
    print(0)
