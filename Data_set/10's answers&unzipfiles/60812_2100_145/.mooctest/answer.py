class Solution:
    def trailingZeroes(self, n):
        if n == 0:
            return 0
        else:
            return int(n/5)+self.trailingZeroes(int(n/5))
a = input()
s = Solution()
print(s.trailingZeroes(int(a)))