class Solution:
    def minCostToMoveChips(self, chips) -> int:
        count0 = 0
        count1 = 0
        for i in chips:
            if i%2 == 0:
                count0+=1
            else:
                count1+=1
        return min(count0,count1)
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.minCostToMoveChips(c))