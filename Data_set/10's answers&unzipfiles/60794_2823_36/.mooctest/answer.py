n, m = map(int, input().split())
dp = [[0]*(n+1) for i in range(m+1)]
dp[0][1] = 1
for i in range(1, m+1):
    for j in range(1, n+1):
        for k in range(j, n+1, j):
            dp[i][k] = (dp[i][k] + dp[i-1][j]) % 1000000007

ans = 0
for i in range(1, n+1):
    ans = (ans + dp[m][i]) % 1000000007

print(ans)
