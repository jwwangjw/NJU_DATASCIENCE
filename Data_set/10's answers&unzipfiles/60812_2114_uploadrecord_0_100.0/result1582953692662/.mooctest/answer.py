class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = {0: 0}
        x = 1
        for i in range(1, n + 1):
            if i == x ** 2:
                x += 1
                f[i] = 1
            else:
                f[i] = min([1 + f[i - j ** 2] for j in range(1, x)])
        return f[n]
a = input()
s = Solution()
print(s.numSquares(int(a)))