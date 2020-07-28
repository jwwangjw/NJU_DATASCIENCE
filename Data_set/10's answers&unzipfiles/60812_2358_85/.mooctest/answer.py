t = int(input())
while t>0:
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    s = ""
    while k>0:
        s += str(a[n-1])
        s += " "
        n -= 1
        k -= 1
    print(s)   
    t -= 1