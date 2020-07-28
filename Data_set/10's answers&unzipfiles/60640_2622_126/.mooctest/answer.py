class Solution:
    def majorityElement(self, nums) -> int:
        nums.sort()
        return nums[int(len(nums)/2)]
b2 = input().split(',')
c2= []
for i in b2:
    c2.append(int(i))
s = Solution()
print(s.majorityElement(c2))