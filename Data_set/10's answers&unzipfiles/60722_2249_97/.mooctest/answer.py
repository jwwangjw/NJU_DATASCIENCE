class Solution:
    def projectionArea(self, grid):
        return sum([sum(map(max, grid)), sum(map(max, zip(*grid))), sum(v > 0 for row in grid for v in row)])
num = int(input().strip())
n = []
for i in range(num):
    b = input().split(',')
    c = []
    for i in b:
        c.append(int(i))
    n.append(c)
s = Solution()
print(s.projectionArea(n))