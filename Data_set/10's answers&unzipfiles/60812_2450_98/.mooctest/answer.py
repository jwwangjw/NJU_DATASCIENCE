class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        if nums and target in nums:
            index = nums.index(target)
            return [index, nums.count(target)+index-1]
        else:
            return [-1, -1]
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
a = int(input())
s = Solution()
print(s.searchRange(c,a))