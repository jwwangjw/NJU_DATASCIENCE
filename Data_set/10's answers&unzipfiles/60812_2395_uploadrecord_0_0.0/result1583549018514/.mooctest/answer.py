for i in range(int(input())):
    n=int(input())
    a=list(map(int , input().split()))
    
    for j in range(n-1) :
        if a[j+1]==a[j] and a[j]!=0 :
            a[j]=a[j]+a[j]
            a[j+1]=0
    
    first=0
    last=n-1
    
    for k in range(n):
        if a[k]!=0 :
            a[first] , a[k] = a[k] , a[first]
            first+=1
    
    a=list(map(str , a))
    
    print(" ".join(a))