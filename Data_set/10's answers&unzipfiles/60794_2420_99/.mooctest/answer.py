class Solution:
    def getNoZeroIntegers(self, n: int):
        def valid(num):
            if num == 0:
                return True
            resid = num % 10
            if resid == 0:
                return False
            else:
                return valid(num//10)

        for i in range(1, n):
            if valid(i) and valid(n-i):
                return [i, n-i]
a = int(input())
s = Solution()
print(s.getNoZeroIntegers(a))