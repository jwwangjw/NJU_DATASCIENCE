class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        lis=[]
        for l in matrix:
            lis+=l
        lis.sort()

        return lis[k-1]
num = int(input().strip())
n = []
for i in range(num):
    b = input().split(',')
    c = []
    for i in b:
        c.append(int(i))
    n.append(c)
a = int(input())
s = Solution()
print(s.kthSmallest(n,a))
