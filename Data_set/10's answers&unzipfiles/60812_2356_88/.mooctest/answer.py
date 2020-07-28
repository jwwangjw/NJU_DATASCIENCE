for i in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    big=a[0]
    f=0
    for i in range(1,n-1):
        if a[i]>=big:
            big=a[i]
            if a[i]<=min(a[i+1:]):
                print(a[i])
                f=1
                break
    if f==0:
        print(-1)
        