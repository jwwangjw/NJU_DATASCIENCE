class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        if n==1:
            return 10
        res = 10
        f = 9
        i = 2
        while i<=n and i<=10:
            f = f*(10-i+1)
            res+=f
            i+=1
        return res
a = input()
s = Solution()
print(s.countNumbersWithUniqueDigits(int(a)))