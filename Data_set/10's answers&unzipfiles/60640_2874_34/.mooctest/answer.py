n = int(input())
# no, code, gym
dp = [[500, 500, 500] for i in range(n+1)]
dp[0][0] = 0
for i, x in enumerate(map(int, input().split()), 1):
    dp[i][0] = min(dp[i-1]) + 1
    if x in (1, 3):  # code
        dp[i][1] = min(dp[i-1][::2])
    if x in (2, 3):  # gym
        dp[i][2] = min(dp[i-1][:2])

print(min(dp[n]))
