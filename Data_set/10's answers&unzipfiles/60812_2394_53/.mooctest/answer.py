for mnm in range (int(input())):
    n=int(input())
    a=map(int,input().split())
    count=0
    for i in a:
        if i!=0:
            print(i,end=' ')
            count+=1
    for i in range(n-count):
        print(0,end=' ')
    print('')