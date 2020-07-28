import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        # 即求小于等于n的完全平方数的个数
        return math.floor(math.sqrt(n))
a = input()
s = Solution()
print(s.bulbSwitch(int(a)))