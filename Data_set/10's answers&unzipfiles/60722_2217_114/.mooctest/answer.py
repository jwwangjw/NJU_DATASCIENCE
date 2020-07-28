class Solution:
    def validSquare(self, p1, p2, p3, p4) -> bool:
        dis = []
        p = [p1, p2, p3, p4]

        for i in range(len(p)):
            for j in range(i+1, len(p)):
                tmp = (p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2
                dis.append(tmp)
        # 如果正方形，那么六个距离只能有两种情况，要么是4条边 要么是2条对角线  经过排序之后，那么前四个距离是边长  后两个距离是对角线
        # 如果只校验边长，那么可能是菱形   所以需要判断一下对角线长度是否相等
        dis.sort()
        return True if dis[0] > 0 and dis[0] == dis[3] and dis[4] == dis[5] else False
b1 = input().split(',')
c1= []
for i in b1:
    c1.append(int(i))
b2 = input().split(',')
c2 = []
for i in b2:
    c2.append(int(i))
b3 = input().split(',')
c3 = []
for i in b3:
    c3.append(int(i))
b4 = input().split(',')
c4 = []
for i in b4:
    c4.append(int(i))
s = Solution()

print(s.validSquare(c1,c2,c3,c4))