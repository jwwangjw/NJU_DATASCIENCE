class Solution:
    def addDigits(self, num: int) -> int:
        if num > 9:
            num = num % 9
            if num == 0:
                return 9
        return num
a = input()
s = Solution()
print(s.addDigits(int(a)))