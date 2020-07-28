class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n%4==0:
            return False
        else:
            return True
d = int(input())
s = Solution()
print(s.canWinNim(d))