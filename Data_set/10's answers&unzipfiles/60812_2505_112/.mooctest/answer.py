class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (sum(nums)-sum(set(nums)))//(len(nums) - len(set(nums)))
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.findDuplicate(c))