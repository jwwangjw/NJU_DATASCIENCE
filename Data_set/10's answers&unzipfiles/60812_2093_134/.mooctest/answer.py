import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def mul(n):
            if n <= 1:
                return 1
            else:
                return n * mul(n - 1)

        l = list(range(1, n + 1))
        res = []
        while l:
            a = mul(len(l) - 1)
            tmp = math.ceil(k / a) - 1
            value = l[tmp]
            res.append(value)
            l.remove(value)
            k = k - tmp * a
        res = list(map(str, res + l))
        return ''.join(res)
a = input()
b = input()
s = Solution()
print(s.getPermutation(int(a), int(b)))
