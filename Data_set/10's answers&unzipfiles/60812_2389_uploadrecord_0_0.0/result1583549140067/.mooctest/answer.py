t=int(input())
while t>0:
    n=int(input())
    a=list(map(str,input().split()))
    for i in range(0,n-1,2):
        temp=(a[i])
        a[i]=a[i+1]
        a[i+1]=temp
    print(' '.join(map(str,a)))
    t=t-1
        