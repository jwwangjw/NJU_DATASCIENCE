class Solution:
    def integerBreak(self, n: int) -> int:
        pre = [1, 2, 4, 6, 9]
        if n < 7:
            return pre[n-2]
        pre = pre[2:]
        for _ in range(n-6):
            pre=pre[1:]+[3*pre[0]]
        return pre[-1]
a = input()
s = Solution()
print(s.integerBreak(int(a)))