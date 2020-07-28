class Solution:
    def findMin(self, nums) -> int:
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]: return nums[i+1]
        return nums[0]
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.findMin(c))