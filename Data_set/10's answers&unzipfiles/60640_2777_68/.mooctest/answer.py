t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    m=(len(a)-1)//2
    if len(a)%2!=0:
        print(a[m])
    else:
        print((a[m]+a[m+1])//2)