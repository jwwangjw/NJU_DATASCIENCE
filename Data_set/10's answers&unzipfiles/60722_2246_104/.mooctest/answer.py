class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        m=[sorted(list(str(2**i))) for i in range(30)]
        if sorted(list(str(N))) in m:
            return True
        else:
            return False
a = int(input())
s = Solution()
print(s.reorderedPowerOf2(a))
