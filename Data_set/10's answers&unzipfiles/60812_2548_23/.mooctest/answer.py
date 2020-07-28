def f(s,k):
    a=[0 for i in range(26)]
    b=[0 for i in range(26)]
    l=[]
    i=0;d=0;
    o=-1
    n=len(s)
    if(n<k):
        return -1
    while(i<n):
        if(a[ord(s[i])-97]==0):
            a[ord(s[i])-97]=1
            d+=1
            l.append(s[i])
            b[ord(s[i])-97]=i
        else:
            a[ord(s[i])-97]+=1
        if(d>k):
            ind=0
            le=len(l)
            for i in range(1,le):
                if(b[ord(l[i])-97]<b[ord(l[ind])-97]):
                    ind=i
            return max(o,f(s[b[ord(l[ind])-97]+1:],k))
        if(d==k):
            o=max(o,i)
        i+=1
    return o
t=int(input())
while(t>0):
    t-=1
    s=input()
    k=int(input())
    p=f(s,k)
    if(p==-1):
        print(-1)
    else:
        print(p+1)