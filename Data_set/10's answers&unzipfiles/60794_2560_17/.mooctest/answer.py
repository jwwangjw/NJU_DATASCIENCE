z=0
t=int(input())
while z<t :
    le=int(input())
    l=list(map(int,input().split()))
    m=int(input())
    l.sort()
    ne=[]
    i=0
    while i< le :
        k=l.count(l[i])
        i=i+k
        ne.append(k)
    ne.sort()
    if len(ne) == 0 :
        print(0) 
    else:
        while m>=ne[0] :
            m=m-ne[0]
            del(ne[0])
            if len(ne)==0 :
                break
        print(len(ne))
    z=z+1