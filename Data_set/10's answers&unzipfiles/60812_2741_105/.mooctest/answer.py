src=eval(input())
dp=[0 for n in range(len(src))]
dp[0]=1
for i,a in enumerate(src):
    dp[i]=1
    if a > src[i-1]:
        dp[i]+=dp[i-1] 
print(max(dp))