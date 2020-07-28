class Solution:
    def numMovesStones(self, a: int, b: int, c: int):
        a, b, c = sorted([a,b,c])
        return [1 if ((b-a == 2) or (c-b == 2)) else (b-a != 1) + (c-b != 1), c-a-2]
b = int(input())
c = int(input())
d = int(input())
s = Solution()
print(s.numMovesStones(b,c,d))