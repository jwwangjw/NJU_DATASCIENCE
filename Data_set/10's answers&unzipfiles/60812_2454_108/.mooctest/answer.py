class Solution(object):
    def findMin(self, nums):
        return min(nums)
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.findMin(c))