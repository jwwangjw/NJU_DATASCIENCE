class Solution:
    def largestPerimeter(self, A) -> int:
        A.sort(reverse=True)
        i = 0
        while len(A) >= 3 and i < len(A) - 2:
            if self.triangle(A[i:i + 3]):
                return sum(A[i:i + 3])
            else:
                i += 1
        return 0

    def triangle(self, nums):
        edge1, edge2, edge3 = nums[0], nums[1], nums[2]
        if (edge1 + edge2 > edge3) and (edge1 + edge3 > edge2) and (edge2 + edge3 > edge1):
            return True
        return False
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.largestPerimeter(c))