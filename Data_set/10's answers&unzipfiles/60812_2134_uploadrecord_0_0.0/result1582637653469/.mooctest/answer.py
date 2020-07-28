import math
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(math.log(buckets)/math.log(minutesToTest//minutesToDie+1))
a = int(input())
b = int(input())
c = int(input())
s = Solution()
print(s.poorPigs(a,b,c))