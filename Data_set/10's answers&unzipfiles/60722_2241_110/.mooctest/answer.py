class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        if N<=2:
            return 1
        c=0
        for x in range(1,N):
           s=x*(x+1)//2
           if s<N:
               if (N-s)%x==0:
                   c+=1
           elif s==N:
               c+=1
               break
           else:
               break
        return c
a = int(input())
s = Solution()
print(s.consecutiveNumbersSum(a))