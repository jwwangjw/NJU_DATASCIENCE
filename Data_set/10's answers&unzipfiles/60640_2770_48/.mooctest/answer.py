for test in range(int(input())):
    n=int(input())
    ar = [[0,0,0] for j in range(n)]
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    for i in range(n):
        ar[i][0]=start[i]
        ar[i][1]=end[i]
        ar[i][2]=i+1
    ar = sorted(ar,key=lambda l:l[1])
    end_time = ar[0][1]
    print(ar[0][2],end=" ")
    for i in range(1,n):
        if end_time < ar[i][0]:
            end_time=ar[i][1]
            print(ar[i][2],end=" ")
    print()
