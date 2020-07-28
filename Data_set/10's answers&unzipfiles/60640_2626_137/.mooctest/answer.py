class Solution:
    def maxCoins(self, nums) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for k in range(2, n):
            for i in range(n - k):
                j = i + k
                for t in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[t] * nums[j] + dp[i][t] + dp[t][j])
        return dp[0][n - 1]
b2 = input().split(',')
c2= []
for i in b2:
    c2.append(int(i))
s = Solution()
print(s.maxCoins(c2))