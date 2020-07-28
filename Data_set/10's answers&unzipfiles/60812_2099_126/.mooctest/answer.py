class Solution(object):
    def titleToNumber(self, s):
        #26进制转10进制
        ans = 0
        for x in s:
            ans *= 26
            ans += ord(x)-ord('A')+1
        return ans
a = input()
s = Solution()
print(s.titleToNumber(a))
