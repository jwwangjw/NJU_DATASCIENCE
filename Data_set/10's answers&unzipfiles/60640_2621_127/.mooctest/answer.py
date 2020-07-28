class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         """
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)
b2 = input().split(',')
c2= []
for i in b2:
    c2.append(int(i))
s = Solution()
print(s.maxSubArray(c2))