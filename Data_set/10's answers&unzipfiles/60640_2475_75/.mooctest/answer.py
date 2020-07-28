t= int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    maxc = 0
    count = 1
    if len(a) == 1:
        maxc = 1
    for i in range(len(a)-1):
        if a[i+1] == a[i] + 1:
            count += 1
        
        else:
            count = 1
        
        if count > maxc:
                maxc = count
        
        
    t -= 1
    print(maxc)