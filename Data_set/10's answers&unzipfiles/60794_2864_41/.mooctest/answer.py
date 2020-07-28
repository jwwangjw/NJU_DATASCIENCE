from collections import defaultdict
n = int(input())
d = defaultdict(int)
for i in map(int, input().split()):
    d[i] += 1
l = max(d.keys()) + 1
dp = [0] * l
dp[1] = d[1]
# choose i-1 --> i has no score
# choose i-2 --> i-1 has no score, i has score
for i in range(2, l):
    dp[i] = max(dp[i-1], dp[i-2] + d[i] * i)
print(dp[l-1])
