class Solution(object):
    def sumSubseqWidths(self, A):
        A.sort()
        sums=0
        for i in range(len(A)):
            sums=sums+(pow(2,i,1000000007)-pow(2,len(A)-1-i,1000000007))*A[i]
        return sums%1000000007
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.sumSubseqWidths(c))