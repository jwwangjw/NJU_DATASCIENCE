t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    l=[0]*(max(a)+1)
    for j in a:
        l[j]+=1
    while(l.count(0)!=len(l)):
        print(((str(l.index(max(l))))+' ')*l[l.index(max(l))],end='')
        l[l.index(max(l))]=0
    print()
        