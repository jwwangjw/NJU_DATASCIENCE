class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        left = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
        right = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
        return left > 0 and right > 0
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
b1 = input().split(',')
c1= []
for i in b1:
    c1.append(int(i))

s = Solution()
print(s.isRectangleOverlap(c,c1))