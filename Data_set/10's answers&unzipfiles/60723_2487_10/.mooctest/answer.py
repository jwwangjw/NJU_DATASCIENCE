t=int(input())
while(t>0):
    t-=1
    n=int(input())
    s=input().split(' ')
    a=[]
    b=[]
    for i in range(n):
        if(s[i] in a):
            k=a.index(s[i])
            b[k]+=1
        else:
            a.append(s[i])
            b.append(1)
    x=''
    c=0
    le=len(a)
    for i in range(le):
        if(b[i]>c or (b[i]==c and a[i]<x)):
            x=a[i]
            c=b[i]
    print(x,c)