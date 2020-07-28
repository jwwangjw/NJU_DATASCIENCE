import math
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = math.gcd(p, q)
        p = p // g & 1
        q = q // g & 1
        return 1 + q - p
a = int(input())
b = int(input())
s = Solution()
print(s.mirrorReflection(a,b))