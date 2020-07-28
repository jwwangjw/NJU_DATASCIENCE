class Solution:
    def ordinalOfDate(self, date: str) -> int:
        y, m, d = map(int, date.split('-'))
        a = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if y != 1900 and y % 4 ==0:
            a[2] += 1
        return sum(a[: m]) +d
a = input()
s = Solution()
print(s.ordinalOfDate(a))