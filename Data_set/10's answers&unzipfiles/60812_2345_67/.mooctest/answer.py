t=int(input())
for _ in range(t):
    n=int(input())
    rep=0
    mis=0
    a=input().split()
    m=[0]*(n+1)
    for i in a:
        i=int(i)
        if(m[i]!=-1):
            m[i]=-1
        else:
            rep=i
    for j in range(1,n+1):
        if (m[j]==0):
            mis=j
    print(rep,end=" ")
    print(mis)