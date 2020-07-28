T=int(input())
for i in range(T):
    N=int(input())
    P=list(map(int,input().split()))
    #P=[int(i) for i in input().split()]
    Q=P
    #print(P)
    for k in range(len(P)-1):
        l=k+1
        ele=-1
        '''while(l<len(P)):
            if P[l]<P[k]:
                ele=P[l]
                break'''
        if P[l]<P[k]:
            ele=P[l]
        Q[k]=ele
    Q[len(P)-1]=-1
    for i in Q:
        print(i,end=" ")
    print()