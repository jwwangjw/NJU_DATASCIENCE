class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min1 = m;
        min2 = n;
        for list in ops:
            min1 = min(min1, list[0])
            min2 = min(min2, list[1])
        return min1 * min2
m = int(input())
nn = int(input())
num = int(input().strip())
n = []
for i in range(num):
    b = input().split(',')
    c = []
    for i in b:
        c.append(int(i))
    n.append(c)
s = Solution()
print(s.maxCount(m,nn,n))
