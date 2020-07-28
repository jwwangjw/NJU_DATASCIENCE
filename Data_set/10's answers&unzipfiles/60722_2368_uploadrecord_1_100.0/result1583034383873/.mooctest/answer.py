def func(N,li):
    max=N-1
    min=0
    lit=[0 for i in range(N)]
    for i in range(N):
        if(i%2==0):
            lit[i]=li[max]
            max=max-1
        else:
            lit[i]=li[min]
            min=min+1
    for k in range(N):
        print(lit[k],end=" ")
    print()
    
    
t=int(input())
for i in range(t):
    N=int(input())
    li=list(input().split())
    func(N,li)