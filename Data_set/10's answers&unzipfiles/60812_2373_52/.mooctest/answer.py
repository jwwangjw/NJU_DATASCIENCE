def sol():
    n=int(input())
    a=list(map(int,input().split()))
    dp=[0]*(n+1)
    dp[1]=a[0]
    
    for i in range(1,n):
        dp[i+1] = max(a[i]+dp[i-1], dp[i])
        
    print(dp[n])
    
t=int(input())
for i in range(t):
    sol()
    