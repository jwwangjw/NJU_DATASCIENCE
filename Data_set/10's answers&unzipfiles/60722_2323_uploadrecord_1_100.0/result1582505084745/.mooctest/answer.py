class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        a=max(A)
        b=min(A)
        if a-b<=2*K:
            return 0
        else:
            return a-b-2*K
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
a = int(input())
s = Solution()
print(s.smallestRangeI(c,a))