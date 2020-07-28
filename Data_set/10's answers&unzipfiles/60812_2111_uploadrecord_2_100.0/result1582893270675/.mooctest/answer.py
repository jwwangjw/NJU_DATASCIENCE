class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        idx2 = 0
        idx3 = 0
        idx5 = 0
        for i in range(n-1):
            res.append(min(res[idx2]*2,res[idx3]*3,res[idx5]*5))
            if res[-1] == res[idx2]*2:
                idx2 += 1
            if res[-1] == res[idx3]*3:
                idx3 += 1
            if res[-1] == res[idx5]*5:
                idx5 += 1
        return res[-1]
a = input()
s = Solution()
print(s.nthUglyNumber(int(a)))