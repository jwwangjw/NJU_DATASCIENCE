class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        return sum(max(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1])) for i in range(1, len(points)))
num = int(input().strip())
n = []
for i in range(num):
    b = input().split(',')
    c = []
    for i in b:
        c.append(int(i))
    n.append(c)
s = Solution()
print(s.minTimeToVisitAllPoints(n))
