class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return [.5, 1.][n == 1]
a = int(input())
s = Solution()
print("%.5f" % s.nthPersonGetsNthSeat(a))