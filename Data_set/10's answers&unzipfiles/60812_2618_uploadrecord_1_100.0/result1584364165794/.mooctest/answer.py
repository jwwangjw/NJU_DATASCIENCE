t=int(input())
for j in range(t):
    n=int(input())
    l=[int(y) for y in input().split()]
    c=[-1]*(n+1)
    for i in range(n):
        c[l[i]]=i
    #print(c)
    maxi=0
    i=1
    while i<n:
        count=1
        while i<n and c[i]<c[i+1]:
            count+=1
            i+=1
        #print(i)
        if maxi<count:
            maxi=count
        i+=1
    print(n-maxi)
        