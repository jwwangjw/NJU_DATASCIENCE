import math
class Solution:
    def numSquarefulPerms(self, A) -> int:
        res = []
        A.sort()
        self.helper(A, [], res)
        return len(res)

    def helper(self, nums, curr, res):
        if not nums:
            res.append(curr)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if len(curr) == 0 or math.sqrt(curr[-1] + nums[i]) % 1 == 0:
                self.helper(nums[:i] + nums[i + 1:], curr + [nums[i]], res)
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.numSquarefulPerms(c))