t=int(input())
for _ in range(t):
    a=input()
    n=len(a)
    s=2**n
    l=[0]*n
    k=[]
    for q in range(1,s):
        x=bin(q)[2:]
        m=l[:]
        r=n-1
        for w in range(len(x)-1,-1,-1):
            m[r]=int(x[w])
            r-=1
        h=[]
        for z in range(n):
            if m[z]==1:
                h.append(a[z])
        k.append(''.join(h))
    f=[]
    for q in k:
        size=len(q)
        if q[0]=='a' or q[0]=='e' or q[0]=='i' or q[0]=='o' or q[0]=='u':
            if not (q[size-1]=='a' or q[size-1]=='e' or q[size-1]=='i' or q[size-1]=='o' or q[size-1]=='u'):
                if q not in f:
                    f.append(q)
    f=sorted(f)
    if len(f)==0:
        print(-1)
    else:
        print(*f)