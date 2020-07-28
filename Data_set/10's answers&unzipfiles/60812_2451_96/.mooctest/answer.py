class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
a = int(input())
s = Solution()
print(s.searchInsert(c,a))