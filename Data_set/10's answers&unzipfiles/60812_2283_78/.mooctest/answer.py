T=int(input())
while T>0:
    a=int(input())
    b=input()
    c=sorted(b)
    d=[]
    for i in range(len(c)):
        if (c[i]=='0' or c[i]=='1' or c[i]=='2'):
            d.append(c[i])
    
    print(' '.join(d))
    T=T-1