class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        ini_point = coordinates[0]
        if coordinates[1][0] - ini_point[0] == 0:
                slope1 = 9999999
        else:
                slope1 = (coordinates[1][1] - ini_point[1])/(coordinates[1][0] - ini_point[0])
        for i in range(1,len(coordinates)):
            if coordinates[i][0] - ini_point[0] == 0:
                slope2 = 9999999
            else:
                slope2 = (coordinates[i][1] - ini_point[1])/(coordinates[i][0] - ini_point[0])
            if slope1 != slope2:
                return False
            slope1 = slope2
        return True
num = int(input().strip())
n = []
for i in range(num):
    b = input().split(',')
    c = []
    for i in b:
        c.append(int(i))
    n.append(c)
s = Solution()
print(s.checkStraightLine(n))
