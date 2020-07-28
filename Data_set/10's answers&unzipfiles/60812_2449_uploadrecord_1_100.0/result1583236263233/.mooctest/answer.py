class Solution:
    def search(self, nums, target: int) -> int:
            return nums.index(target) if target in nums else -1
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
a = int(input())
s = Solution()
print(s.search(c,a))