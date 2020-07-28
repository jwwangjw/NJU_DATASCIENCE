from math import gcd
class Solution:
    def isGoodArray(self, nums) -> bool:
        if len(nums)==1:
            return nums[0]==1
        res=nums[0]
        for i in range(1,len(nums)):
            res = gcd(res, nums[i])
            if res==1:
                return True
        return False
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.isGoodArray(c))