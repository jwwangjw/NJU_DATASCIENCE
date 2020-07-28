class Solution:
    def largestTriangleArea(self, points) -> float:
        from itertools import combinations
        amax=0
        for i in combinations(points,3):
            x = [i[0][0], i[1][0], i[2][0]]
            y = [i[0][1], i[1][1], i[2][1]]
            s = abs((x[0]-x[2])*(y[1]-y[2])-(x[1]-x[2])*(y[0]-y[2]))/2
            amax=max(s,amax)
        return amax
num = int(input().strip())
n = []
for i in range(num):
    b = input().split(',')
    c = []
    for i in b:
        c.append(int(i))
    n.append(c)
s = Solution()
print(s.largestTriangleArea(n))