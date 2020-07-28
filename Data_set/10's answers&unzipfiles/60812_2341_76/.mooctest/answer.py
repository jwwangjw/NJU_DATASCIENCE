for _ in range(int(input())):
    X,Y=input().split()
    X=int(X)
    Y=int(Y)
    aa=[]
    b=[]
    aa=input().split()
    b=input().split()
    c=aa+b
    x=[int(x) for x in c]
    to=sorted(x)
    for i in to:
        print(i,end=' ')
    print()