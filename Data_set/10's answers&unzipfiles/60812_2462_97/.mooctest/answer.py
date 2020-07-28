class Solution:
    def findPeakElement(self, nums) -> int:
        start = nums[0]
        n = len(nums)
        if n==1: return 0
        for i in range(1, n):
            if nums[i] > start:
                start = nums[i]
            else:
                return i-1
        return i
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.findPeakElement(c))