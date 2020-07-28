T=int(input())
while(T>0):
    a=int(input())
    s=input()
    d={}
    f=0
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    #print(d)
    for i in s:
        if d[i]==1:
            f=1
            break
    if f==0:
        print(-1)
    else:
        print(i)
    T=T-1